import idaapi

x = 0
while x < 2000:
    idaapi.step_over()
    GetDebuggerEvent(WFNE_SUSP, -1)
    rv = idaapi.regval_t()
    idaapi.get_reg_val('EIP', rv)
    ea = rv.ival
    print hex(ea)
    x += 1

'''
1000
100
'''
