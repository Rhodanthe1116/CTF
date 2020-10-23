#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *

r = remote('140.112.31.97', 30001)

n = int(r.recvline().split(b' = ')[1])
c = int(r.recvline().split(b' = ')[1])
e = 65537

_3e = pow(3, e, n)

L, R = 0, 1
for i in range(1024):
    c = (c * _3e) % n
    r.sendline(str(c))
    m = int(r.recvline().split(b' = ')[1])
    L, R = L * 3, R * 3

    if m == 0:
        R -= 2
    if m == 1:
        L += 1
        R -= 1
    if m == 2:
        L += 2

print(long_to_bytes(L * n // (3**1024)))
print(long_to_bytes(R * n // (3**1024)))
