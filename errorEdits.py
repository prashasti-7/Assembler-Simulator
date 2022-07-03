#to store value in 16- bit register
r0 = []
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []

flags = []
for i in range(16):
    flags.append(0)

l=[]
final_print=[]
var_list = []
count = 1
error_list=[]
def dec_to_bi(n):
    st=''
    while n!=0:
        r=int(n)%2
        st=st+str(r)
        n=int(n)//2
        p=st[::-1]
    return(p)

l=[]
def bi_to_dec(l):           
    k = len(l)             
    sum = 0
    for i in range(k):                
        sum = sum + l[k-i-1]*(2**i)
    return sum

op_code={'add':'10000','sub':'10001','mov':{1:'10010',2:'10011'},'ld':'10100',
        'st':'10101','mul':'10110','div':'10111','rs':'11000',
        'ls':'11001','xor':'11010','or':'11011','and':'11100',
        'not':'11101', 'cmp':'11110','jmp':'11111','jlt':'01100',
        'jgt':'01101','je':'01111','hlt':'01010'}                      #'mov':10010--->immediate  'mov':10011--->register   

reg_code={'R0':'000','R1':'001','R2':'010','R3':'011',
'R4':'100','R5':'101','R6':'110','FLAGS':'111'}    

reg_val = {'R0': r0, 'R1': r1, 'R2':r2, 'R3': r3, 'R4':r4, 'R5':r5, 'R6':r6, 'FLAGS': flags}
while(True):
    inp=list(map(str,input().split()))

    # Type A:
    if(inp[0]=='add'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            count = count + 1
            final_print.append(op_code['add']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
            value1 = bi_to_dec(reg_val[inp[1]])
            value2 = bi_to_dec(reg_val[inp[2]])
            sum=value1+value2
            sum=dec_to_bi(sum)
            reg_val[inp[3]]=sum

            if (value1+value2>255):
                flags[12]==1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)
                # error handling for wrong input
    elif(inp[0]=='sub'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            count = count + 1
            final_print.append(op_code['sub']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
            value1 = bi_to_dec(reg_val[inp[1]])
            value2 = bi_to_dec(reg_val[inp[2]])
            diff=value1-value2
            diff=dec_to_bi(diff)
            reg_val[inp[3]]=diff
            if (value1-value2<0):
                flags[12]==1
                reg_val[inp[3]]='00000000'

        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)

    elif(inp[0]=='mul'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            count = count + 1            
            final_print.append(op_code['mul']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
            value1 = bi_to_dec(reg_val[inp[1]])
            value2 = bi_to_dec(reg_val[inp[2]])
            prod=value1*value2
            prod=dec_to_bi(prod)
            reg_val[inp[3]]=prod
            if (value1*value2>255):
                flags[12]==1
                
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)

    elif(inp[0]=='xor'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            count = count + 1            
            final_print.append(op_code['xor']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)
 
    elif(inp[0]=='or'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            count = count + 1            
            final_print.append(op_code['or']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)
   
    elif(inp[0]=='and'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            count = count + 1            
            final_print.append(op_code['and']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)

    # Type B:
    elif(inp[0]=='mov'):
        if(inp[1] in reg_code):
            word = inp[2]
            word_list = list(word)
            if(word_list[0]=='$'):
                count = count + 1
                word_list.remove('$')
                word_final = ''.join(word_list)
                if (int(word_final)>255 or int(word_final)<0):
                    error_list.append("Immediate value invalid. Line "+count)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                final_print.append(op_code['mov'][1] + reg_code[inp[1]] + t + value)
                for i in range(16-length):
                    reg_val[inp[1]].append(0)
                for i in value:
                    reg_val[inp[1]].append(i)

            else:
                if(inp[2] in reg_code):  #Type C
                    count = count + 1
                    final_print.append(op_code['mov'][2] + '00000' + reg_code[inp[1]] + reg_code[inp[2]] )
                    reg_val[inp[2]] = reg_val[inp[1]].copy()
                else:
                    error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)
    
    elif(inp[0]=='ls'):
        if(inp[1] in reg_code):
            word = inp[2]
            word_list = list(word)
            if(word_list[0]=='$'):
                count = count + 1
                word_list.remove('$')
                word_final = ''.join(word_list)
                if (int(word_final)>255 or int(word_final)<0):
                    error_list.append("Immediate value invalid. Line "+count)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                final_print.append(op_code['ls'] + reg_code[inp[1]] + t + value)
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)
        

    elif(inp[0]=='rs'):
        if(inp[1] in reg_code):
            word = inp[2]
            word_list = list(word)
            if(word_list[0]=='$'):
                count = count + 1
                word_list.remove('$')
                word_final = ''.join(word_list)
                if (int(word_final)>255 or int(word_final)<0):
                    error_list.append("Immediate value invalid. Line "+count)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                final_print.append(op_code['rs'] + reg_code[inp[1]] + t + value)            
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)    

    # Type C:
    elif(inp[0]=='div'):
        if(inp[1] in reg_code and inp[2] in reg_code):
            count = count + 1
            final_print.append(op_code['div']+'00000' + reg_code[inp[1]] + reg_code[inp[2]])   
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)         

    elif(inp[0]=='not'):
        if(inp[1] in reg_code and inp[2] in reg_code):
            count = count + 1            
            final_print.append(op_code['not']+'00000' + reg_code[inp[1]] + reg_code[inp[2]])
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)         

    elif(inp[0]=='cmp'):
        if(inp[1] in reg_code and inp[2] in reg_code):
            count = count + 1            
            final_print.append(op_code['cmp']+'00000' + reg_code[inp[1]] + reg_code[inp[2]])  
            value1 = bi_to_dec(reg_val[inp[1]])
            value2 = bi_to_dec(reg_val[inp[2]])
            if(value1 < value2):
                flags[13] == 1
            elif(value1 > value2):
                flags[14] == 1
            elif(value1 == value2):
                flags[15] == 1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)

    #Type D
    elif(inp[0]=='ld'):
        if(inp[1] in reg_code):
            count = count + 1             
            final_print.append(op_code['ld'] + reg_code[inp[1]] + value)     ######doubt
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)

    elif(inp[0]=='st'):
        if(inp[1] in reg_code):
            count = count + 1        
            final_print.append(op_code['st'] + reg_code[inp[1]] + value)     ######doubt
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+count)

    #Type E
    elif(inp[0]=='jmp'):
        count = count + 1                
        final_print.append(op_code['jmp'] + '000' + value)     ######doubt

    elif(inp[0]=='jlt'):
        count = count + 1
        final_print.append(op_code['jlt'] + '000' + value)     ######doubt

    elif(inp[0]=='jgt'):
        count = count + 1
        final_print.append(op_code['jgt'] + '000' +  value)     ######doubt      

    elif(inp[0]=='je'):
        count = count + 1
        final_print.append(op_code['je'] + '000' + value)     ######doubt   

    #Type F
    elif(inp[0]=='hlt'):
        count = count + 1
        final_print.append(op_code['hlt']+'00000000000')
        break

    elif(inp[0]=='var'):
        var_list. append(inp[1])
    
    else:
        error_list.append("Incorrect instruction.")
if (len(error_list>0)):
    print(error_list[0])
    #print(*error_list,sep='\n')
print(*final_print,sep='\n')
print(*var_list)
