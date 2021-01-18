obj = [].__class__.__base__

# can call function in f''
test = f"{obj.__subclasses__()}"
'''
<class 'type'>, <class 'weakref'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'int'>, <class 'bytearray'>, <class 'bytes'>,
'''

# cannot call function in .format
# this will cause an error
test = "{obj.__subclasses__}".format(obj=obj)
'''
AttributeError: type object 'object' has no attribute '__subclasses__()'
'''

# cannot call function in .format
# this will cause an error
test = "{a.}".format(a=[])
print(test)
'''
AttributeError: type object 'object' has no attribute '__subclasses__()'
'''

# cannot call function in .format again
# test = "{a.abs(-1)} ".format(a=[])
# AttributeError: 'list' object has no attribute 'abs(-1)'

# # cannot call function in .format again
# test = "{(lambda: None)} ".format(a=[])
# # print(test)
