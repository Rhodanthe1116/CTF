import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


m = 'my name is benson.'
key = get_random_string(len(m))
print('密鑰', key)

c = ''
for i in range(len(m)):
    c += chr(ord(m[i]) ^ ord(key[i]))

# （看不到，不是printable_ascii）
print('密文', c)
# （bytes）
print('密文', bytes(c, 'ascii'))
# hex
print('密文', bytes(c, 'ascii').hex())
# output:
#
m = ''
for i in range(len(c)):
    m += chr(ord(c[i]) ^ ord(key[i]))

print('明文', m)
