#!/usr/bin/env python
# coding=utf-8
from pwn import *
import sys

for action_code in range(100):
    r = process('./sudoku')

    r.recvuntil("Press ENTER to start......\n")
    r.sendline('enter')
    r.sendline('enter')

    ans = [
        '8', '1', '2', '7', '5', '3', '6', '4', '9',
        '9', '4', '3', '6', '8', '2', '1', '7', '5',
        '6', '7', '5', '4', '9', '1', '2', '8', '3',
        '1', '5', '4', '2', '3', '7', '8', '9', '6',
        '3', '6', '9', '8', '4', '5', '7', '2', '1',
        '2', '8', '7', '1', '6', '9', '5', '3', '4',
        '5', '2', '1', '9', '7', '4', '3', '6', '8',
        '4', '3', '8', '5', '2', '6', '9', '1', '7',
        '7', '9', '6', '3', '1', '8', '4', '5', '2'
    ]

    for cell in ans:
        r.sendline(cell)
        r.sendline('l')

    r.sendline('z')
    # r.recvuntil(b"ACTION CODE:\n")
    r.sendline(str(action_code))
    r.recvuntil('ACTION CODE:\n')
    r.recvline('\n')
    result = r.recvline('\n')
    print(result)
    ok = result != b"You are not the agent.....\n"
    print(ok)

    # r.interactive()
    r.close