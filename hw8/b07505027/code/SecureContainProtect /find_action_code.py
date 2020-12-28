import string
total_ans = 257498

f = open("./flag")
encoded_flag = f.read().split()
assert(len(encoded_flag) == 6015)

for i in range(len(encoded_flag)):
    encoded_flag[i] = int(encoded_flag[i], 16)
encoded_flag = list(map(int, encoded_flag))

f = open("./s1")
s1 = f.read().split()
print(len(s1))
assert(len(s1) == 3161)

f = open("./s2")
s2 = f.read().split()
assert(len(s2) == 169)


for i in range(len(s1)):
    s1[i] = int(s1[i], 16)
s1 = list(map(int, s1))


for i in range(len(s2)):
    s2[i] = int(s2[i], 16)
s2 = list(map(int, s2))


ans = [
    '8', '1', '2', '7', '5', '3', '6', '4', '9',
    '9', '4', '3', '6', '8', '2', '1', '7', '5',
    '6', '7', '5', '4', '9', '1', '2', '8', '3',
    '1', '5', '4', '2', '3', '7', '8', '9', '6',
    '3', '6', '9', '8', '4', '5', '7', '2', '1',
    '2', '8', '7', '1', '6', '9', '5', '3', '4',
    '5', '2', '1', '9', '7', '4', '3', '6', '8',
    '4', '3', '8', '5', '2', '6', '9', '1', '7',
    '7', '9', '6', '3', '1', '8', '4', '5', '2'
]
ans = list(map(int, ans))

w = 32
for i in range(len(encoded_flag)):
    encoded_flag[i] = encoded_flag[i] ^ ans[i % 81]

def get_flag(action_code):
    total = 0
    new_flag = [0] * len(encoded_flag)
    for i in range(len(encoded_flag)):
        new_flag[i] = encoded_flag[i] ^ ord(
            action_code[i % len(action_code)])
        if chr(new_flag[i]) not in string.printable:
            pass
            # return False
        total += new_flag[i]

    flag_str = ''
    for i in new_flag:
        flag_str += chr(i)

    # print(total)
    if total == 257498:
        print('found: ', flag_str)
        return flag_str

def get_flag_without_check(action_code):
    total = 0
    new_flag = [0] * len(encoded_flag)
    for i in range(len(encoded_flag)):
        new_flag[i] = encoded_flag[i] ^ ord(
            action_code[i % len(action_code)])
        total += new_flag[i]

    return new_flag, total

def find_min_action_code(w):
    action_code = ''
    for i in range(w):     
        min_total = 1e10
        min_c = '😊'
        inputable = string.printable
        for c in inputable:
            total = 0
            
            ok = True
            for j in range(i, len(encoded_flag), w):
                res = encoded_flag[j] ^ ord(c)
                total += res
                if chr(res) not in string.printable:
                    ok = False
                    break

            if not ok: 
                continue
            
            if total < min_total:
                min_total = total
                min_c = c

            
        action_code += min_c
    return action_code

def print_flag(flag):
    print('-----------FLAG-------------')

    a = bytes(flag)
    print(a.decode('utf-8'))

    print('----------------------------')

def print_flag_raw(flag, w):
    for i in range(len(flag)):
        c = chr(flag[i])

        # if c == '\n':
        #     print()
        # elif c == ' ':
        #     print(c, end='')
        # elif c in string.ascii_uppercase:
        #     print('A', end='')
        # elif c in string.ascii_lowercase:
        #     print('a', end='')
        if c in '\n\t\r\b\f\v':
            print('$', end='')
        elif c not in string.printable:
            print('$', end='')
        else:
            print(c, end='')
        
        if i % w == 0:
            print()
        
    print()


for i in range(len(s1)):
    s1[i] = s1[i] ^ ans[i % 81]
print(bytes(s1).decode('utf-8'))

for i in range(len(s2)):
    s2[i] = s2[i] ^ ans[i % 81]
print(bytes(s2).decode('utf-8'))
print()

print('----------------')

print_flag_raw(encoded_flag, 128)
a = ''.join(chr(i) for i in encoded_flag)
for i in range(0, len(a), w):
    print(ascii(a[i:i+w]))

print('----------------------------')
print('----------------------------')

for w in range(1, 40):
    action_code = find_min_action_code(w)
    print(action_code)
    flag, total = get_flag_without_check(action_code)
    print('total: ', total)
    # print_flag(flag)
    if total == total_ans:
        print_flag(flag)

"decrypt_the_document_of_SCP-2521"