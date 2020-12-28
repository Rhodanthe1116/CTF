import string
ll = []
f = open("./bur")
raw_bur = f.read().split()

bur = []
for i in range(len(raw_bur)):
    if i % 5 == 0:
        continue
    bur += [int(raw_bur[i][2:], 16)]
bur = list(map(int, bur))

'''
func 0 0 0 
num5  num2 step  num3 
'''
func_list = bur[::10]
num5_list = bur[4::10]
num2_list = bur[5::10]
step_list = bur[6::10]
num3_list = bur[7::10]
num4_list = bur[8::10]

num3_list = [num3 & 0xffffffff for num3 in num3_list]
num4_list = [num4 & 0xffffffff for num4 in num4_list]

# print(func_list[:50])
# print(num5_list[:50])
print(num2_list[:140])
print(step_list[:140])
print(num3_list[:50])
print(num4_list[:50])
print(list(map(hex, num3_list[:100])))
print(list(map(hex, num4_list[:100])))

# 0x400FBA == 4198330
print(set(num2_list[:70]))

func_list = [hex(func_list[i] + num5_list[i]) for i in range(len(func_list))]
print(func_list[:10])
print(set(func_list[:1000]))


f = open("./flag")
encoded_flag = f.read().split()
assert(len(encoded_flag) == 70)
for i in range(len(encoded_flag)):
    encoded_flag[i] = int(encoded_flag[i], 16)
encoded_flag = list(map(int, encoded_flag))

f = open("./fib")
fib = f.read().split()
fib = list(map(int, fib))

def invfib(sum):
    return fib.index(sum) + 1

f = open("./facebook")
fb = f.read().split()
fb = list(map(int, fb)) 

def facebook(sum):
    return fb.index(sum) + 1

flag = encoded_flag
count = 0

for t in range(1000):
    # input
    # print(f't = {t}')
    # c = input()
    # serial = [c] + ['0'] * 69
    serial = [0] * 70
    seriala = [0] * 70
    

    i = 0
    while i < 70:
        # print(f'i = {i}')
        num2 = num2_list[count]
        step = step_list[count]
        num3 = num3_list[count]
        num4 = num4_list[count]

        func = func_list[count]

        for j in range(step):
            a = 32
            b = num3 if j == 0 else num4
            # a = serial[num2 + j] 
            # print(f'a = {a}')
            # b = *((_DWORD *)&serial + j + 4LL + 1) )
            if func == '0x4011d6':
                a = invfib(b)
            elif func == '0x40102d':
                v1 = 0
                for k in range(200):
                    if k & 1:
                        v1 += 2
                    else:
                        v1 += 11
                    if v1 == b:
                        a = k + 1
                        break
                # b = v1

                # a = (b // 13) * 2 - b % 13 + 1
            elif func == '0x400fbe':
                a = b // 135
            elif func == '0x4010c8':
                a = (b ^ 1383424633)
            elif func == '0x401138':
                a = facebook(b)
                
                
            else:
                print('exception')
                exit()

            if chr(a) not in string.ascii_uppercase and chr(a) not in string.digits:
                print(func)
            
            # print(f'b = {b}')
            serial[num2 + j] = a
            # print(serial)
         
        count += 1
        i += step
    # print(len(seriala))
    # print(serial)
    # print(len(serial))
    
    print(*list(map(chr, serial)), sep='')

    for i in range(70):
        flag[i] = flag[i] ^ serial[i]

print('flag is')
flag = list(map(chr, flag))
print(*flag, sep='')
