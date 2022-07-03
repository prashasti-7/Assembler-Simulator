def dec_to_bi(n):
    st=''
    while n!=0:
        r=int(n)%2
        st=st+str(r)
        n=int(n)//2
        p=st[::-1]
    return(p)

op_code={'add':'10000','sub':'10001','mov':{1:'10010',2:'10011'},'ld':'10100',
        'st':'10101','mul':'10110','div':'10111','rs':'11000',
        'ls':'11001','xor':'11010','or':'11011','and':'11100',
        'not':'11101', 'cmp':'11110','jmp':'11111','jlt':'01100',
        'jgt':'01101','je':'01111','hlt':'01010'}                      #'mov':10010--->immediate  'mov':10011--->register   

reg_code={'R0':'000','R1':'001','R2':'010','R3':'011',
'R4':'100','R5':'101','R6':'110','FLAGS':'111'}    

input_list = []
final_print = []
i = 0

while(True):
    inp=list(map(str,input().split()))
    input_list.append(inp)
    if('hlt' in inp):
        break

len_list = len(input_list)
var_count = 0
var_dict = {}

# Type A
if(input_list[i][0]=='add'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
        final_print.append(op_code['add']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])
        i+=1
            # error handling for wrong input 

elif(input_list[i][0]=='sub'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
        final_print.append(op_code['sub']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])
        i+=1

elif(input_list[i][0]=='mul'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
        final_print.append(op_code['mul']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])
        i+=1

elif(input_list[i][0]=='xor'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
        final_print.append(op_code['xor']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])
        i+=1

elif(input_list[i][0]=='or'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
        final_print.append(op_code['or']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])
        i+=1

elif(input_list[i][0]=='and'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
        final_print.append(op_code['and']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])
        i+=1

# Type B
elif(input_list[i][0]=='mov'):
        if(input_list[i][1] in reg_code):
            word = input_list[i][2]
            word_list = list(word)
            if(word_list[0]=='$'):
                word_list.remove('$')
                word_final = ''.join(word_list)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                final_print.append(op_code['mov'][1] + reg_code[input_list[i][1]] + t + value)
                i+=1

            else:
                if(input_list[i][2] in reg_code):  #Type C
                    final_print.append(op_code['mov'][2] + '00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] )
                    i+=1

elif(input_list[i][0]=='ls'):
    if(input_list[i][1] in reg_code):
        word = input_list[i][2]
        word_list = list(word)
        if(word_list[0]=='$'):
            word_list.remove('$')
            word_final = ''.join(word_list)
            decimal_number = str(word_final)
            value = dec_to_bi(decimal_number)
            value  = str(value)
            length = len(value)
            t = '0'*(8-length)
            i+=1
            final_print.append(op_code['ls'] + reg_code[input_list[i][1]] + t + value)

elif(input_list[i][0]=='rs'):
    if(input_list[i][1] in reg_code):
        word = input_list[i][2]
        word_list = list(word)
        if(word_list[0]=='$'):
            word_list.remove('$')
            word_final = ''.join(word_list)
            decimal_number = str(word_final)
            value = dec_to_bi(decimal_number)
            value  = str(value)
            length = len(value)
            t = '0'*(8-length)
            i+=1
            final_print.append(op_code['rs'] + reg_code[input_list[i][1]] + t + value)

 # Type C:
elif(input_list[i][0]=='div'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
        i+=1
        final_print.append(op_code['div']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])            

elif(input_list[i][0]=='not'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
        i+=1           
        final_print.append(op_code['not']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])         

elif(input_list[i][0]=='cmp'):
    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
        i+=1         
        final_print.append(op_code['cmp']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])         

#Type D
elif(input_list[i][0]=='ld'):
    if(input_list[i][1] in reg_code):
        if(input_list[i][2] in var_dict):
            i+=1 
            final_print.append(op_code['ld'] + reg_code[input_list[i][1]] + var_dict[input_list[i][2]])     ######doubt

elif(input_list[i][0]=='st'):
    if(input_list[i][1] in reg_code):
        if(input_list[i][2] in var_dict):
            i+=1
            final_print.append(op_code['st'] + reg_code[input_list[i][1]] + var_dict[input_list[i][2]])     ######doubt

#value
elif(input_list[i][0]=='var'):
    var_count+=1
    # i+=1
    value = var_count + len_list
    var_dict.update({input_list[i][1]:value})

print(input_list)
print(*final_print,sep='\n')
