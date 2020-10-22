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


def int_to_bitlist(n):
    return [int(i) for i in f'{n:016b}']


def bitlist_to_bytes(l):
    s = ''.join(map(str, l))
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')


output = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1,
          0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]

LFSR_LEN = 16

lsfr_feedbacks = [39989, 40111, 52453]

# LFSR3 > LFSR2 > LFSR1(x)
for feedback in reversed(lsfr_feedbacks):

    # 只找當前準確度最大值
    max_accuracy = 0.70
    best_init = [0] * LFSR_LEN

    for inits in range(2**LFSR_LEN+5):
        inits_list = int_to_bitlist(inits)

        # generate
        lfsr = LFSR(inits_list, [int(i) for i in f'{feedback:016b}'])
        lfsr_output = [lfsr.getbit() for _ in range(100)]

        # metrics
        correct = 0
        for i in range(len(output)):
            if lfsr_output[i] == output[i]:
                correct += 1

        accuracy = correct / len(output)
        if accuracy >= max_accuracy:
            max_accuracy = accuracy
            best_init = inits_list
            print(accuracy)
            print(inits_list)
            print(bitlist_to_bytes(best_init))

        # 輸出目前暴搜到多少了（0~65535）
        if inits % 10**3 == 0:
            print(inits)

        inits += 1

    print(bitlist_to_bytes(best_init))
    # b'hj'
    # b'ui'
    # b'o\xc4'

# FLAG{XXuihj}
