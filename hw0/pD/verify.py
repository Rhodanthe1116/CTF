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

    print(f'_加密前: 向量: {向量}, 累加: {累加}')
    for t in range(32):
        累加 = 累加 + 得優塔 & 遮罩
        向量[0] = 向量[0] + ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累加) & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
        向量[1] = 向量[1] + ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累加) & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
        print(f'_加密{t}: 向量: {向量}, 累加: {累加}')
    return 向量


def _解密(向量: List[int], 金鑰: List[int]):
    累減 = 1507197312
    # 跑程式算累加的最終值
    # for _ in range(32):
    #     累減 += 得優塔 & 遮罩
    # print(hex(累減))
    得優塔 = 0xFACEB00C
    遮罩 = 0xffffffff

    print(f'_解密前: 向量: {向量}, 累減: {累減}')
    for t in range(32):
        向量[1] = 向量[1] - ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累減) & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
        向量[0] = 向量[0] - ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累減) & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
        累減 = 累減 - 得優塔 & 遮罩
        print(f'_解密{t}: 向量: {向量}, 累加: {累減}')
    return 向量

def 加密(明文: bytes, 密鑰: bytes):
    密文 = b''
    # 格式：abcdefghABCDEFGH
    for 索引 in range(0, len(明文), 8):
        # 密文 += 逆轉換(_加密(正轉換(明文[索引:索引+8]), 正轉換(密鑰)))
        正轉換後密鑰 = 正轉換(密鑰)
        print('正轉換後密鑰: ', 正轉換後密鑰)
        正轉換後明文一半 = 正轉換(明文[索引:索引+8])
        print('正轉換後明文一半: ', 正轉換後明文一半)
        加密後 = _加密(正轉換後明文一半, 正轉換後密鑰)
        print('加密後: ', 加密後)
        逆轉換後 = 逆轉換(加密後)
        print('逆轉換後: ', 逆轉換後)
        密文 += 逆轉換後
        print('密文: ', 密文)
    return 密文

def 解密(密文: bytes, 密鑰: bytes):
    明文 = b''
    # 格式：abcdefghABCDEFGH
    for 索引 in range(0, len(密文), 8):
        正轉換後密鑰 = 正轉換(密鑰)
        print('正轉換後密鑰: ', 正轉換後密鑰)
        正轉換後密文一半 = 正轉換(密文[索引:索引+8])
        print('正轉換後密文一半: ', 正轉換後密文一半)
        解密後 = _解密(正轉換後密文一半, 正轉換後密鑰)
        print('解密後: ', 解密後)
        逆轉換後 = 逆轉換(解密後)
        print('逆轉換後: ', 逆轉換後)
        明文 += 逆轉換後
        print('明文: ', 明文)
    return 明文

if __name__ == '__main__':
    # 先用假的flag明文測試
    旗幟 = b'flag{abcdefghij}'
    print(f'旗幟 = {旗幟.hex()}')
    print()
    assert len(旗幟) == 16
    
    random.seed(int(time.現在()))
    密鑰 = random.給我random位元們(128).to_bytes(16, 'big')
    print(f'密鑰: {密鑰}')
    # 密鑰格式 = b'FFFFFFFFFFFFFFFF'
    
    密文 = 加密(旗幟, 密鑰)
    print(f'密文 = {密文.hex()}')
    print()
   
    明文 = 解密(密文, 密鑰)
    print(f'明文 = {明文.hex()}')
    print()
    
    print('驗證成功？', 旗幟 == 明文)

############################

# 底下是研究各函數的過程

# import random as random
# random.給我random位元們 = random.getrandbits
# random位元們 = random.給我random位元們(128)
# 密鑰 = random位元們.to_bytes(16, 'big')
# print(random位元們)
# # 91596674949567904657985019240082561359
# print(密鑰)
# # b'D\xe8\xe0\xbe\xa7\xbc%\n\x00e(^\x89\xaf\xd9O'
# # abcdabcdabcdabcd


# def 正轉換(資料, 大小=4):
#     # [abcd, abcd, abcd, abcd]
#     return [int.from_bytes(資料[i:i+大小], 'big') for i in range(0, len(資料), 大小)]

# print(正轉換(密鑰))
# # [1292374909, 3920341056, 1827551618, 3331993363]

# 明文 = b'0101010101010101'
# print(正轉換(明文[0:0+8]))
# # [808529969, 808529969]

# # _加密([808529969, 808529969], [1292374909, 3920341056, 1827551618, 3331993363])
# def _加密(向量: List[int], 金鑰: List[int]):
#     累加 = 0
#     得優塔 = 0xFACEB00C
#     遮罩 = 0xffffffff
#     print(hex(累加 + 得優塔 & 遮罩))
#     # 0xfaceb00c
#     for _ in range(32):
#         累加 = 累加 + 得優塔 & 遮罩
#         # 得優塔 & 遮罩 = 4207849484
#         向量[0] = 向量[0] + ((向量[1] << 4) + 金鑰[0] & 遮罩 ^ (向量[1] + 累加) & 遮罩 ^ (向量[1] >> 5) + 金鑰[1] & 遮罩) & 遮罩
#         向量[1] = 向量[1] + ((向量[0] << 4) + 金鑰[2] & 遮罩 ^ (向量[0] + 累加) & 遮罩 ^ (向量[0] >> 5) + 金鑰[3] & 遮罩) & 遮罩
#     return 向量

# 累加 = 0
# 得優塔 = 0xFACEB00C
# 遮罩 = 0xffffffff

# 累加 = 累加 + 得優塔 & 遮罩
# print(hex(累加))
# # 0xfaceb00c
# 累加 = 累加 + 得優塔 & 遮罩
# print(hex(累加))
# # 0xf59d6018
# 累加 = 累加 + 得優塔 & 遮罩
# print(hex(累加))
# # 0xf06c1024

# print(808529969 << 4)
# # 12936479504
# _加密(正轉換(明文[0:0+8]), 正轉換(密鑰))
