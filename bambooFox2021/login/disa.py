import dis
s = b'd\x01d\x02d\x03d\x04d\x05d\x06d\x03d\x07d\x06d\x08d\x03d\td\nd\nd\x0bd\x0cd\rg\x11}\x00t\x00j\x01\xa0\x02d\x0e\xa1\x01t\x00j\x01\xa0\x02d\x0f\xa1\x01t\x00j\x01\xa0\x02d\x10\xa1\x01g\x03\x89\x00\x88\x00d\x11\x19\x00t\x03|\x00d\x12\x19\x00\x83\x01k\x02r\x9c\x88\x00d\x13\x19\x00t\x03|\x00d\x14\x19\x00\x83\x01k\x02r\x9c\x88\x00d\x15\x19\x00d\x16k\x02r\x9cd\x17d\x18\xa0\x04t\x05\x87\x00f\x01d\x19d\x1a\x84\x08|\x00\x83\x02\xa1\x01\x17\x00d\x1b\x17\x00S\x00d\x1cS\x00'
dis.dis(s)

const = (None, 247, 254, 216, 225, 234, 243, 244, 245, 228, 
232, 235, 166, 184, #14
'give', 'me', 'flag', #15 16 17
0, 3, 1, -3, 2,  #22
'\x87', 'flag{', '', #25
< code object < lambda > at 0x7f9fce0710e0, file "./main.py", line 15 > , 
'get_flag.<locals>.<lambda>', 
'}', 
'NO FLAG FOR YOU')

co_name = ('request', 'args', 'get', 'str', 'join', 'map')
con_varname = ('magic',),

STORE_FAST = sss
34 BUILD_LIST              17

co_names[0] = 'request'

         0 LOAD_CONST               1 (1)
          2 LOAD_CONST               2 (2)
          4 LOAD_CONST               3 (3)
          6 LOAD_CONST               4 (4)
          8 LOAD_CONST               5 (5)
         10 LOAD_CONST               6 (6)
         12 LOAD_CONST               3 (3)
         14 LOAD_CONST               7 (7)
         16 LOAD_CONST               6 (6)
         18 LOAD_CONST               8 (8)
         20 LOAD_CONST               3 (3)
         22 LOAD_CONST               9 (9)
         24 LOAD_CONST              10 (10)
         26 LOAD_CONST              10 (10)
         28 LOAD_CONST              11 (11)
         30 LOAD_CONST              12 (12)
         32 LOAD_CONST              13 (13)
         34 BUILD_LIST              17
         36 STORE_FAST               0 (0)      co_varnames= magic = [12321jwqdqwndo]
         38 LOAD_GLOBAL              0 (0)    'request'
         40 LOAD_ATTR                1 (1)      'args'
         42 <160>                    2
         44 LOAD_CONST              14 (14)     give
         46 <161>                    1
         48 LOAD_GLOBAL              0 (0)       'request'
         50 LOAD_ATTR                1 (1)      'args'
         52 <160>                    2
         54 LOAD_CONST              15 (15)     me
         56 <161>                    1
         58 LOAD_GLOBAL              0 (0)
         60 LOAD_ATTR                1 (1)      'args'
         62 <160>                    2
         64 LOAD_CONST              16 (16)     flag
         66 <161>                    1
         68 BUILD_LIST               3

        ['give', 'me', 'flag']
         70 STORE_DEREF              0 (0)
         72 LOAD_DEREF               0 (0)
         74 LOAD_CONST              17 (17)     0 give
         76 BINARY_SUBSCR                           a[0]
         78 LOAD_GLOBAL              3 (3)      get str
         80 LOAD_FAST                0 (0)      magic
         82 LOAD_CONST              18 (18)     3
         84 BINARY_SUBSCR                       magic[3]
        
         86 CALL_FUNCTION            1
         88 COMPARE_OP               2 (==)
         90 POP_JUMP_IF_FALSE      156
         
         92 LOAD_DEREF               0 (0)
         94 LOAD_CONST              19 (19)     1, me
         96 BINARY_SUBSCR
         98 LOAD_GLOBAL              3 (3)      get str
        100 LOAD_FAST                0 (0)      magic
        102 LOAD_CONST              20 (20)     -3
        104 BINARY_SUBSCR                       magic[-3]

        106 CALL_FUNCTION            1
        108 COMPARE_OP               2 (==)
        110 POP_JUMP_IF_FALSE      156

        112 LOAD_DEREF               0 (0)
        114 LOAD_CONST              21 (21)     2 flag
        116 BINARY_SUBSCR                       a[2]
        118 LOAD_CONST              22 (22)     '\x87'
        120 COMPARE_OP               2 (==)
        122 POP_JUMP_IF_FALSE      156
        
        okok
        124 LOAD_CONST              23 (23)
        126 LOAD_CONST              24 (24)
        128 <160>                    4
        130 LOAD_GLOBAL              5 (5)      map
        132 LOAD_CLOSURE             0 (0)
        134 BUILD_TUPLE              1
        136 LOAD_CONST              25 (25)
        138 LOAD_CONST              26 (26)
        140 MAKE_FUNCTION            8
        142 LOAD_FAST                0 (0)
        144 CALL_FUNCTION            2
        146 <161>                    1
        148 BINARY_ADD
        150 LOAD_CONST              27 (27)
        152 BINARY_ADD
        154 RETURN_VALUE
