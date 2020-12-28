#!/usr/bin/env python
# coding=utf-8
from pwn import *
import sys

r = process('/home/hwww/CTF/hw7/Going Crazy/gogo')

arr = [0] * 36
indexes = [15, 32, 1, 29, 23, 18, 14, 31, 26, 8, 27, 2, 16, 20, 21, 34,
           19, 28, 24, 22, 5, 7, 3, 25, 6, 0, 13, 12, 30, 11, 33, 9, 35, 10, 17, 4]

for index in indexes:

    for num in range(1, 150):
        # if i == 114: continue
        arr[index] = num
        str_arr = list(map(str, arr))
        payload = 'x' + ','.join(str_arr) + 'x'
        # print(payload)

        r.recvuntil("Say something :\n")
        r.sendline(payload)
        reply = r.recvline()
        this_ok = reply == b"No!!!That's way too crazy!!Stop!!\n"

        if this_ok:
            break

        end = reply == b'CRAZY!CRAZIER!CRAZIEST!!\n'
        if end:
            break

print(payload)
ans = list(map(chr, arr))
print(*ans, sep='')

r.interactive()

# x70,76,65,71,124,103,111,103,111,95,112,48,119,101,114,114,52,110,103,51,114,33,121,111,117,95,100,105,100,95,73,84,33,33,33,125x
