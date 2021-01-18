import os
import string
import subprocess

sh = subprocess.check_output
'''
.data:00000000006B9100	00000041	C	vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~o

'''
table = "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~o"

encoded_flag = 'U?w>'
print(len(encoded_flag), 'len of encoded_flag')

options = list(string.printable)
options.remove('`')
options.remove('"')

flag = ['g', ' ', '2']
for c in options:
    flag[1] = c
    input_str = "".join(flag)
    print(input_str)
    res = sh(f'./JustOnLinux "{input_str}"', shell=True)
    res = res.decode()
    print(res)
    print(encoded_flag)
    if (res == encoded_flag):
        print('yes')
        break

    if c == options[-1]:
        print('no')
        exit()
