regcode = ['R0','R1','R2','R3','R4','R5','R6']
address_reg = ['000','001','010','011','100','101','110','111']
regcode_dict = dict(zip(regcode, address_reg))
print(regcode_dict)

opcode = ['10000','10001','10010','10011','10100','10101','10110','10111','11000','11001','11010','11011','11100','11101','11110','11111','01100','01101','01111','01010']
ist = ['add','sub','mov','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']
opcode_dict = dict(zip(opcode, ist))
print(opcode_dict)

while(True):
    inp = list(map(str,input().split())) 
    if (inp[0]=='add'):
        print("WOW")