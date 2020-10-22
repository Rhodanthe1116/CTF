#!/usr/bin/env python3
from functools import reduce


class LFSR:
    def __init__(self, init, feedback):
        self.state = init
        self.feedback = feedback

    def getbit(self):
        nextbit = reduce(lambda x, y: x ^ y, [
                         i & j for i, j in zip(self.state, self.feedback)])
        self.state = self.state[1:] + [nextbit]
        return nextbit


class MYLFSR:
    def __init__(self, inits):
        inits = [
            [int(i) for i in f"{int.from_bytes(init, 'big'):016b}"] for init in inits]
        self.l1 = LFSR(inits[0], [int(i) for i in f'{39989:016b}'])
        self.l2 = LFSR(inits[1], [int(i) for i in f'{40111:016b}'])
        self.l3 = LFSR(inits[2], [int(i) for i in f'{52453:016b}'])

    def getbit(self):
        x1 = self.l1.getbit()
        x2 = self.l2.getbit()
        x3 = self.l3.getbit()
        return (x1 & x2) ^ ((not x1) & x3)

    def getbyte(self):
        b = 0
        for i in range(8):
            b = (b << 1) + self.getbit()
        return bytes([b])


def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])


def int_to_bitlist(n):
    return [int(i) for i in f'{n:016b}']


def bitlist_to_bytes(l):
    s = ''.join(map(str, l))
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')


output = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1,
          0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]

LFSR_LEN = 16

lsfr_feedbacks = [39989]
init1 = '' # unknown
init2 = b'ui'
init3 = b'hj'

# 只找當前準確度最大值
max_accuracy = 0.80
best_init = [0] * LFSR_LEN
for init1 in range(2**LFSR_LEN+5):
    inits_list = int_to_bitlist(init1)

    # generate
    lfsr = MYLFSR([bitlist_to_bytes(inits_list), init2, init3])
    lfsr_output = [lfsr.getbit() for _ in range(100)]

    # metrics
    correct = 0
    for i in range(len(output)):
        if lfsr_output[i] == output[i]:
            correct += 1
    accuracy = correct / len(output)

    # 更新當前最大值並輸出
    if accuracy >= max_accuracy:
        max_accuracy = accuracy
        best_init = inits_list
        print(accuracy)
        print(inits_list)
        print(bitlist_to_bytes(best_init))

    # 輸出目前暴搜到多少了（0~65535）
    if init1 % 10**3 == 0:
        print(init1)

    init1 += 1

print(bitlist_to_bytes(best_init))
# b'df'

# 大約搜到25000就會找到正解（準確度100%）