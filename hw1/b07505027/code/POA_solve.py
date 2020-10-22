#!/usr/bin/env python3
from pwn import *


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


r = remote("140.112.31.97", 30000)

enc = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())


def oracle(c):
    r.sendlineafter('cipher = ', c.hex())
    if b'YESSSSSSSS' in r.recvline():
        return True
    else:
        return False


PAD = 128
ZERO = 0

flag = b''
for i in range(16, len(enc), 16):
    ans = b''
    iv, block = enc[i-16:i], enc[i:i+16]
    for j in range(16):
        for k in range(256):
            # if you change nothing, padding will be correct,
            # but not the case we want.

            # NOTE: When plain is 0x00, 
            # there will be another solution where k != iv[16 - 1 - j].
            # But when plain is 0x80, this is what we want
            # but we will skip it. So we need to pick it up
            # if we have no solution after every k is checked.
            if k == iv[16 - 1 - j]:
                continue

            if oracle(
                iv[:16 - 1 - j]
                + bytes([k])
                + xor(bytes([ZERO] * j), xor(iv[-j:], ans))
                + block
            ):
                ans = bytes([iv[16 - 1 - j] ^ k ^ PAD]) + ans
                print(ans)
                break

            # no solution found. k == iv[16 - 1 - j] is what we want.
            if k == 255:
                ans = bytes([PAD]) + ans
                print(ans)

    flag += ans

print(flag)
