opCodes={'add':'10000','sub':'10001','mov':['10010','10011'],'ld':'10100',
        'st':'10101','mul':'10110','div':'10111','rs':'11000',
        'ls':'11001','xor':'11010','or':'11011','and':'11100',
        'not':'11101', 'cmp':'11110','jmp':'11111','jlt':'01100',
        'jgt':'01101','je':'01111','hlt':'01010'}                      #'mov':10010--->immediate  'mov':10011--->register   

Registers={'R0':'000','R1':'001','R2':'010','R3':'011',
'R4':'100','R5':'101','R6':'110','FLAGS':'111'}    
while(True):
    inp=list(map(str,input().split()))
    if(inp[0]=='add'):
        if(inp[1]=='reg1'):
            print("wow")
