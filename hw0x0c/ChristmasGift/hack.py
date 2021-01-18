import string

f = open("./data")
raw_data = f.read().split()
print(len(raw_data))
print(raw_data[:20])
data = []
for i in range(len(raw_data)):
    data += [int(raw_data[i], 16)]
data = list(map(int, data))

print(len(data))
print(data[:20])

s2 = 'JZC33MJPDC48UXXJ94BBQOR0JJR4AO0W02PHZ4VZRJAEXL3OUI02FQ4GSQIDGBFT70VESKNAAUEJW4RR9EQOCJ9PKT7W9FBMJDVK6X9MT7K1HY30MSA4H3Y9FTV0O7Z6FQ5I1J8R6KSCMWKFSDGCMWARIJTLPLRO8KUYQW2F46ZV6YWIVFNCZDQRCTAM5JVGQMEU2LFPS5DUDOY4130XB50V91PWHCIO0AD1RHTR673DPX36TA2UWA48FD34Y2W6'
s3 = '_'
print(len(s2))
data = data[:3360731]
assert(len(data) == 3360731)
for i in range(3360731):
    data[i] ^= ord(s2[i % len(s2)])
    # data[i] ^= ord(s3[i % len(s3)])
    # print(data)

# output
print('after XOR')
print(data[:100])
flag = list(map(chr, data))
print(*flag[:100], sep='')

for c in flag[:100]:
    if c in string.printable[:-5]:
        print(c, end='')
print()

width = 64
for i in range(10000):
    c = flag[i]
    if c in string.printable[:-5]:
        print(c, end='')
    else:
        print('*', end='')
    if i % width == width - 1:
        print()
print()

d = {}
for c in flag:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

for k, v in d.items():
    print([k], v)
# for i in range(1000):
#     c = flag[i]
#     print(chr(ord(c) ^ ord(' ')), end='')


f = open("./output")
output = f.read()
print((output[:100]))

print(bytes(data[:1000]))
