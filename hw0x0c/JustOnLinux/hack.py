import os
import string
import subprocess

sh = subprocess.check_output
table = "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~o"
encoded_flag = 'M&=wM].]VyA?GR&[GRA%I]Q#HOA_GRz/T%M?H?T@UR_%HBL?GRA.U?w>HSM*WS@ '
print(len(encoded_flag), 'len of encoded_flag')

# verify
c1 = 'F'
c3 = 'A'
print(table[ord(c1) >> 2 & 63])
print(table[ord(c3) & 63])

options = list(string.printable)

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