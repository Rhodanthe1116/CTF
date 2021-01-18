import os
import string
import subprocess

sh = subprocess.check_output
'''
.data:00000000006B9100	00000041	C	vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~o

'''
table = "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~o"

encoded_flag = 'M&=wM].]VyA?GR&[GRA%I]Q#HOA_GRz/T%M?H?T@UR_%HBL?GRA.U?w>HSM*WS@ '
print(len(encoded_flag), 'len of encoded_flag')

# verify
c1 = 'F'
c3 = 'A'
print(table[ord(c1) >> 2 & 63])
print(table[ord(c3) & 63])

flag = []

options = list(string.printable)
options.remove('`')

blocks = len(encoded_flag) // 4

for t in range(16):
    flag += [chr(32)] * 3

    # find c3
    for c in options:
        encoded_c3 = table[ord(c) & 63]
        if encoded_c3 == encoded_flag[4*t+3]:
            flag[3*t + 2] = c
            break

    # find c1
    for c in options:
        encoded_c1 = table[ord(c) >> 2 & 63]
        if encoded_c1 == encoded_flag[4*t]:
            flag[3*t + 0] = c

            # find c2
            ok = False
            for c2 in options:
                c1 = flag[3*t + 0]
                c3 = flag[3*t + 2]
                c123 = (ord(c1) << 16) + (ord(c2) << 8) + ord(c3)
                encoded_s1 = table[c123 >> 12 & 63]
                encoded_s2 = table[c123 >> 6 & 63]
                if encoded_s1 == encoded_flag[4*t + 1] and encoded_s2 == encoded_flag[4*t + 2]:
                    flag[3*t + 1] = c2
                    ok = True
                    break
                if encoded_s1 == encoded_flag[4*t + 1] and encoded_s2 == chr(ord(encoded_flag[4*t + 2]) - 1):
                    flag[3*t + 1] = c2

            if ok:
                break
            else:
                continue

        if c == options:
            print('no')


for c in string.printable:
    encoded_c1 = table[ord(c) >> 2 & 63]
    if encoded_c1 == encoded_flag[-1]:
        flag += c
        break
    if c == options:
        print('no')


print(*flag, sep='')
res = sh(f'./JustOnLinux "{"".join(flag)}"', shell=True)
res = res.decode()
print(res, 'res')
print(encoded_flag, 'encoded_flag')

inverse = {}
for i in range(len(table)):
    c = table[i]
    inverse[c] = i

print(inverse[encoded_flag[3]] + (1 << 6))

flag = ''
for t in range(15):
    s1 = inverse[encoded_flag[4*t + 0]]
    s2 = inverse[encoded_flag[4*t + 1]]
    s3 = inverse[encoded_flag[4*t + 2]]
    s4 = inverse[encoded_flag[4*t + 3]]
    # find c3
    c1 = (s1 << 2) + ((s2 >> 4) & 3) 
    c2 = ((s2 & 15) << 4) + (s3 >> 2) 
    # print(bin(s2 & 15), bin(s3 >> 2))
    c3 = ((s3 & 3) << 6) + s4 
    flag += chr(c1) + chr(c2) + chr(c3)
    print(flag)

flag += 'm}'
print(flag)

'''
c1 + c2 + c3
 c1000000000000000
        c200000000
                c3
=
------------------
 111111112222222233333333

c1c2c3

c100000c2000000c3
s1 = 00111111 // c1 >> 2
s2 = 11112222
s3 = 22222233
s4 = 33333333

VyA?

'''


# flag = flag + ['0']
#     for c in options:
#         flag[i] = c
#         input_str = "".join(flag)
#         print(input_str)
#         res = sh(f'./JustOnLinux "{input_str}"', shell=True)
#         res = res.decode()
#         print(res, 'res')

#         print('------')
#         print(res[:-1])
#         print(encoded_flag[:len(res)-1])
#         print('------')
#         if (res[:-1] == encoded_flag[:len(res)-1]):
#             print('yes')
#             pre_idx = lres)
#             break

#         if c == options[-1]:
#             print('no')
#             exit()
