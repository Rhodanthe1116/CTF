import string

f = open("./flag")
encoded_flag = f.read().split()
assert(len(encoded_flag) == 6015)

for i in range(len(encoded_flag)):
    encoded_flag[i] = int(encoded_flag[i], 16)
encoded_flag = list(map(int, encoded_flag))

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

def get_flag_without_check(action_code):
    total = 0
    new_flag = [0] * len(encoded_flag)
    for i in range(len(encoded_flag)):
        new_flag[i] = encoded_flag[i] ^ ord(
            action_code[i % len(action_code)])
        total += new_flag[i]

    return new_flag, total

def print_flag_raw(flag, w):
    for i in range(len(flag)):
        c = chr(flag[i])

        if c in '\n\t\r\b\f\v':
            print('$', end='')
        elif c not in string.printable:
            print('$', end='')
        else:
            print(c, end='')
        
        if i % w == 0:
            print()
        
    print()

print('----------------------------')

flag, total = get_flag_without_check("                ")
print_flag_raw(flag, 128)

"decrypt_the_document_of_SCP-2521"