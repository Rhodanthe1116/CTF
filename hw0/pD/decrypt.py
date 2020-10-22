#!/usr/bin/env python3
import time as time
import random as random
from typing import List as List
from io import BufferedReader as 緩衝讀取者
from forbiddenfruit import curse as curse

遮罩 = 0xffffffff
curse(int, "從bytes", int.from_bytes)
curse(int, "到bytes", int.to_bytes)
curse(bytes, "十六進制", bytes.hex)
curse(bytes, "加入", bytes.join)
# curse(緩衝讀取者, "讀取", 緩衝讀取者.read)
random.seed = random.seed
random.給我random位元們 = random.getrandbits
time.現在 = time.time
print = print
open = open
range = range
len = len


def 正轉換(資料, 大小=4):
    return [int.from_bytes(資料[i:i+大小], 'big') for i in range(0, len(資料), 大小)]


def 逆轉換(資料, 大小=4):
    return b''.join([元素.to_bytes(大小, 'big') for 元素 in 資料])


def _加密(向量: List[int], 金鑰: List[int]):
    累加 = 0
    得優塔 = 0xFACEB00C
    遮罩 = 0xffffffff

    for t in range(32):
        累加 = 累加 + 得優塔 & 遮罩
        向量[0] = 向量[0] + ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累加)
                         & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
        向量[1] = 向量[1] + ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累加)
                         & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
    return 向量


def _解密(向量: List[int], 金鑰: List[int]):
    累減 = 1507197312
    得優塔 = 0xFACEB00C
    遮罩 = 0xffffffff

    for t in range(32):
        向量[1] = 向量[1] - ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累減)
                         & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
        向量[0] = 向量[0] - ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累減)
                         & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
        累減 = 累減 - 得優塔 & 遮罩
    return 向量

# 密文 = 加密(旗幟, 密鑰)


def 加密(明文: bytes, 密鑰: bytes):
    密文 = b''
    for 索引 in range(0, len(明文), 8):
        正轉換後密鑰 = 正轉換(密鑰)
        正轉換後明文一半 = 正轉換(明文[索引:索引+8])
        加密後 = _加密(正轉換後明文一半, 正轉換後密鑰)
        逆轉換後 = 逆轉換(加密後)
        密文 += 逆轉換後
    return 密文


def 解密(密文: bytes, 密鑰: bytes):
    明文 = b''
    # abcdefghABCDEFGH
    for 索引 in range(0, len(密文), 8):
        正轉換後密鑰 = 正轉換(密鑰)
        正轉換後密文一半 = 正轉換(密文[索引:索引+8])
        解密後 = _解密(正轉換後密文一半, 正轉換後密鑰)
        逆轉換後 = 逆轉換(解密後)
        明文 += 逆轉換後
    return 明文


if __name__ == '__main__':

    seed = int(time.time())
    t = 0
    while True:
        random.seed(seed)

        # 每搜10**5後輸出目前的狀況
        if (t % 10**5 == 0):
            print(f'seed: {seed}')
            print(time.localtime(seed))

        密鑰 = random.給我random位元們(128).to_bytes(16, 'big')

        密文 = bytes.fromhex('77f905c39e36b5eb0deecbb4eb08e8cb')

        明文 = 解密(密文, 密鑰)

        flag = '666c6167'
        FLAG = '464c4147'

        ok = 明文.hex()[0:8] == flag or 明文.hex()[0:8] == FLAG
        if (ok):
            print('OK!')
            print(f'明文: {明文.hex()}')
            print(f'密鑰: {密鑰.hex()}')
            print()

        # 不安心 輸出一下更寬鬆的比對結果
        maybe = 明文.hex()[0:6] == flag[0:6]
        if (maybe):
            print('maybe!')
            print(f'明文: {明文.hex()}')
            print(f'密鑰: {密鑰.hex()}')
            print()

        seed -= 1
        t += 1
