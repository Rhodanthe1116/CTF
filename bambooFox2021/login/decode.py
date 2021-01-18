f = "w1MEoJZVmhu2u7GWN6V4SJRTUrLQxDJK9MBCWezdtOo"
d = ord('o') - ord('{')
for c in f:
    print(chr(ord(c) - d), end='')
print()

for c in f:
    print(ord(c), end=' ')
print()

f = 'flag{'
for c in f:
    print(ord(c), end=' ')
print()
'''
115d2c2214....12
'''
