from pwn import *

context.terminal =  ['tmux', 'splitw', '-h']
r = process("./hw1")
gdb.attach(r)