global_secret = 'I_am_secret....'

my_list = []

s = dir(my_list)
print(s)

s = my_list.__class__
print(s)

s = my_list.__str__
print(s)
# <method-wrapper '__str__' of list object at 0x7f075d646848>
s = dir(my_list.__str__)
print(s)

s = my_list.__str__.__init__
print(s)

s = dir(my_list.__str__.__init__)
print(s)

s = my_list.__init__
print(s)
# <method-wrapper '__str__' of list object at 0x7f075d646848>
s = dir(my_list.__init__)
print(s)

s = my_list.__init__
print(s)
# <method-wrapper '__init__' of list object at 0x7fcdbfc02848>

s = dir(my_list.__init__)
print(s)
# ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__objclass__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

s = my_list.__init__.__init_subclass__
print(s)

s = my_list.__class__
print(s)

print()
print("============about __globals__, test for class=========")
print()

class Flag():
    flag = "123"

f = Flag()

s = f.__str__
print(s)
# <method-wrapper '__str__' of list object at 0x7f075d646848>
s = dir(f.__str__)
print(s)

# this will cause an error
# s = f.__str__.__globals__
# print(s)


print()
print("============about __globals__, test for class=========")
print()


class Flag2():
    flag = "123"
    def __str__(self):
        # I can have global
        pass


f = Flag2()

s = f.__str__
print(s)

s = dir(f.__str__)
print(s)

s = f.__str__.__globals__
print(s)

s = dir(f.__str__.__globals__)
print(s)

s = f.__str__.__globals__['global_secret']
print(s)

print()
print("============about __globals__ =========")
print()

print("============builtin functions don't have __globals__=========")
print()

s = abs.__init__
# <method-wrapper '__init__' of builtin_function_or_method object at 0x7f870247e630>

# this will cause an error
# s = abs.__init__.__globals__
# AttributeError: 'method-wrapper' object has no attribute '__globals__'

print("============custom functions have __globals__=========")
print()

def g():
    pass

s = g.__globals__
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':

print("============lambda has __globals__=========")
print()

lam = lambda: None
s = lam.__globals__
# {'__name__': '__main__', '__doc__': None, '__package__': None,

print("============imported modules has no attribute __globals__=========")
print()

import math

s = dir(math)
# print(s)
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
'''

# s = dir(math.__globals__)
'''
AttributeError: module 'math' has no attribute '__globals__'
'''

s = dir(math.__loader__)
'''
['__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__',
  '__le__', '__lt__', '__module__', '__ne__', '__new__', 
  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
  'create_module', 'exec_module', 'find_module', 'find_spec',
   'get_code', 'get_source', 'is_package', 'load_module', 'module_repr']
'''


s = math.__loader__.module_repr
'''
['__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__',
  '__le__', '__lt__', '__module__', '__ne__', '__new__', 
  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
  'create_module', 'exec_module', 'find_module', 'find_spec',
   'get_code', 'get_source', 'is_package', 'load_module', 'module_repr']
'''

# s = math.exp.__init__.__globals__
'''
AttributeError: module 'math' has no attribute '__globals__'
'''

# s = math.__builtins__
'''
AttributeError: module 'math' has no attribute '__builtins__'
'''

s = math.__class__.__module__
print(s)
'''
AttributeError: module 'math' has no attribute '__builtins__'
'''

print("============how to let builtin func have __globals__ =========")
print()

f = abs

s = dir(f)
'''
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
'''

s = f.__class__
print(s)
'''
<class 'builtin_function_or_method'>
'''

s = f.__class__
print(s)
'''
<class 'builtin_function_or_method'>
'''

print()
print("============__builtins__ =========")
print()

a = __builtins__

s = dir(a)
# print(s)
'''
['ArithmeticError', 'AssertionError', 'AttributeError'...'type', 'vars', 'zip']

__import__
eval
'''

print("============about __subclasses__ =========")
print()

a = []

# object
o = a.__class__.__base__
# <class 'object'>

s = dir(o)
'''
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''

s = dir(o.__subclasses__)
'''
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
'''

s = o.__subclasses__.__call__()
'''
[<class 'type'>, <class 'weakref'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'int'>, <class 'bytearray'>, <class 'bytes'>, <class 'list'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'traceback'>, <class 'super'>, <class 'range'>,
'''

print("============about __module__ =========")
print()

f = abs

s = f.__module__
'''
builtins
'''

s = g.__code__
print(s)
'''
<code object g at 0x7ff159269270, file "./tutorial.py", line 109>
'''

s = math.sin.__code__
print(s)
'''
<code object g at 0x7ff159269270, file "./tutorial.py", line 109>
'''

flag = '{flag.__str__.__globals__[app].secret_key}'
