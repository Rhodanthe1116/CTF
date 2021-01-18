p = 'a'
payload = [p[i] for i in range(0, len(p))]
a = []
res = f"{a.__class__.__base__.__subclasses__}"

# print(eval("'{" + "\'+\'".join(payload) + "}'"))
# print(eval("( '{" + "\'+\'".join(payload) + "}' ).format(a=[])"))
# print(res)
m = "'{" + "\'+\'".join(payload) + "}'"
# print(m)
# a = eval(m)
# # a2 = "( " + a + " ).format(a=[])"
# print(a)
# print((a).format(a=[]))

print("( " + m + " ).format(a=token_bytes)")
# print("f\"{( " + m + " )}\"")
# ('{a._'+'_cla'+'ss_'+'_'+'}').format(a=[])

# print('{a'+'.'+'_'+'_'+'c'+'l'+'a'+'s'+'s'+'_'+'_'+'.'+'_'+'_'+'b'+'a'+'s'+'e'+'_'+'_' +
#       '.'+'_'+'_'+'s'+'u'+'b'+'c'+'l'+'a'+'s'+'s'+'e'+'s'+'_'+'_'+'('+')}')
