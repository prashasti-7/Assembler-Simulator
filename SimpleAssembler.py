import sys

input_list = []
final_print = []
var_dict = {}
label_dict = {}
i = 0
var_count = 0
k=0
p=0
not_final = []

l=[]
final_print=[]
var_list = []
count = 1
error_list=[]

def dec_to_bi(n):
    p=''
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
        sum = sum + int(l[k-i-1])*(2**i)
    return sum

op_code={'add':'10000','sub':'10001','mov':{1:'10010',2:'10011'},'ld':'10100',
        'st':'10101','mul':'10110','div':'10111','rs':'11000',
        'ls':'11001','xor':'11010','or':'11011','and':'11100',
        'not':'11101', 'cmp':'11110','jmp':'11111','jlt':'01100',
        'jgt':'01101','je':'01111','hlt':'01010'}                      #'mov':10010--->immediate  'mov':10011--->register   

reg_code={'R0':'000','R1':'001','R2':'010','R3':'011',
'R4':'100','R5':'101','R6':'110'}    

# while(True):
#     inp=list(map(str,input().split()))
#     input_list.append(inp)
#     if('hlt' in inp):
#         break

inp = []
with open(sys.argv[1], 'r') as f:
    for lines in f.readlines():
        line = list(map(str,lines.split()))
        lines.rstrip('\n')
        elements = lines.split(' ')
        input_list.append(line)

len_list = len(input_list)

for p in range(len_list):
    if(input_list[p][0]=='var'):
        var_count+=1
    elif(input_list[p][0] in op_code):
        k = p
        break

# for p in range(k+1, len_list):
#     if(input_list[p][0]=='var'):
#         print("Variable not declared at the beginning. Error in Line: " + p)
#         quit()

s = 0
for h in range(len_list):
    if(input_list[h][0] == 'hlt'):
        s = 1

# if(input_list[len_list-1][0] != 'hlt'):
#     print("Halt instruction not at the end. Error in Line " + len_list-1)
#     quit()

for i in range(len_list):
    if (input_list[i][0]=='hlt' and i!=len_list-1):
        print("Halt instruction not at the end. Error in Line " + i)


if (s == 0):
    print("Halt instruction is missing")
    quit()

len_var_list = len_list - var_count

def addInst():
    final_print.append(op_code['add']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])

def subInst():
    final_print.append(op_code['sub']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])

def mulInst():
    final_print.append(op_code['mul']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])

def xorInst():
    final_print.append(op_code['xor']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])

def orInst():
    final_print.append(op_code['or']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])

def andInst():
    final_print.append(op_code['and']+'00' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] + reg_code[input_list[i][3]])

def movInst():
    word = input_list[i][2]
    word_list = list(word)
    if(word_list[0]=='$'):
        word_list.remove('$')
        word_final = ''.join(word_list)
        if (int(word_final)>255 or int(word_final)<0):
            error_list.append("Immediate value invalid. Line "+str(i))
        decimal_number = str(word_final)
        value = dec_to_bi(decimal_number)
        value  = str(value)
        length = len(value)
        t = '0'*(8-length)
        final_print.append(op_code['mov'][1] + reg_code[input_list[i][1]] + t + value)

    else:
        if(input_list[i][2] in reg_code):  #Type C
            final_print.append(op_code['mov'][2] + '00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]] )

        elif(input_list[i][2] == 'FLAGS'):
            final_print.append(op_code['mov'][2] + '00000' + reg_code[input_list[i][1]] + '111')

        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

def lsInst():
    word = input_list[i][2]
    word_list = list(word)
    if(word_list[0]=='$'):
        word_list.remove('$')
        word_final = ''.join(word_list)
        if (int(word_final)>255 or int(word_final)<0):
            error_list.append("Immediate value invalid. Line "+str(i))
        decimal_number = str(word_final)
        value = dec_to_bi(decimal_number)
        value  = str(value)
        length = len(value)
        t = '0'*(8-length)
        final_print.append(op_code['ls'] + reg_code[input_list[i][1]] + t + value)

def rsInst():
    word = input_list[i][2]
    word_list = list(word)
    if(word_list[0]=='$'):
        word_list.remove('$')
        word_final = ''.join(word_list)
        if (int(word_final)>255 or int(word_final)<0):
            error_list.append("Immediate value invalid. Line "+str(i))
        decimal_number = str(word_final)
        value = dec_to_bi(decimal_number)
        value  = str(value)
        length = len(value)
        t = '0'*(8-length)
        final_print.append(op_code['rs'] + reg_code[input_list[i][1]] + t + value)

def divInst():
    final_print.append(op_code['div']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])

def cmpInst():
    final_print.append(op_code['cmp']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])  

# input_list = [list(map(str, line.strip().split(','))) for line in open('Test_Case.txt')]

for i in range(len_list):
    len_inst = len(input_list[i])
    if(input_list[i][0]=='add' and len_inst == 4):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            addInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+ str(i))
            i+=1
            # error handling for wrong input
            
    elif(input_list[i][0]=='sub' and len_inst == 4):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            subInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    elif(input_list[i][0]=='mul' and len_inst == 4):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            mulInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    elif(input_list[i][0]=='xor' and len_inst == 4):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            xorInst()
            i+=1

        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    elif(input_list[i][0]=='or' and len_inst == 4):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            orInst()
            i+=1

        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    elif(input_list[i][0]=='and' and len_inst == 4):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            andInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    # Type B:
    elif(input_list[i][0]=='mov' and len_inst == 3):
        if(input_list[i][1] in reg_code):
            movInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1
    
    elif(input_list[i][0]=='ls' and len_inst == 3):
        if(input_list[i][1] in reg_code):
            lsInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    elif(input_list[i][0]=='rs' and len_inst == 3):
        if(input_list[i][1] in reg_code):
            rsInst()
            i+=1         
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    # Type C:
    elif(input_list[i][0]=='div' and len_inst == 3):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
            divInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))         
            i+=1

    elif(input_list[i][0]=='not' and len_inst == 3):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
            final_print.append(op_code['not']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1 

    elif(input_list[i][0]=='cmp' and len_inst == 3):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
            cmpInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    #Type D
    elif(input_list[i][0]=='ld' and len_inst == 3):
        if(input_list[i][1] in reg_code):
            if(input_list[i][2] in var_list):
                final_print.append(op_code['ld'] + reg_code[input_list[i][1]] + var_dict[input_list[i][2]])    
                i+=1
            else:
                error_list.append("Error! Variable not defined!"+"-"+"Line "+str(i))
                i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    elif(input_list[i][0]=='st' and len_inst == 3):
        if(input_list[i][1] in reg_code):
            if(input_list[i][2] in var_list):
                final_print.append(op_code['st'] + reg_code[input_list[i][1]] + var_dict[input_list[i][2]])     
                i+=1
            else:
                error_list.append("Error! Variable not defined!"+"-"+"Line "+str(i))            
                i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
            i+=1

    #Type E
    elif(input_list[i][0]=='jmp' or input_list[i][0]=='jlt' or input_list[i][0]=='jgt' or input_list[i][0]=='je'):
        if(len_inst == 2):
            if(input_list[i][1] in label_dict):
                final_print.append(op_code[input_list[i][0]] + '000' + label_dict[input_list[i][1]])    
                i+=1  
            else:
                # for g in range(i+1,len_list):
                #     input_list[g][0]= input_list[g][0][:-1]
                #     if(input_list[g][0] == input_list[i][1]):
                #         value = dec_to_bi(g)
                #         value  = str(value)
                #         length = len(value)
                #         t = '0'*(8-length)
                #         final_print.append(op_code[input_list[i][0]] + '000' + t + value)   
                #         i=i+1 
                error_list.append("Error! Format incorrect!"+"-"+"Line "+str(i))
                i+=1

    #Type F
    elif(input_list[i][0]=='hlt'):
        final_print.append(op_code['hlt'] + '00000000000')
        i+=1
        if(i==len_list):
            break

    elif(input_list[i][0]=='var' and len_inst==2):
        # q=0
        var_list.append(input_list[i][1])
        q = var_list.index(input_list[i][1])
        value = len_var_list + q
        value = dec_to_bi(value)
        value  = str(value)
        length = len(value)
        t = '0'*(8-length)
        var_dict.update({input_list[i][1]:t+value})

    elif(input_list[i][0][-1]==':'):
        label_inst = str(input_list[i][0])
        label_inst = label_inst[:-1]
        if(label_inst in reg_code or label_inst in var_list or label_inst in op_code):
            error_list.append("Illegal label name. Line "+str(i))

        else:
            value = dec_to_bi(i-len(var_list))
            value  = str(value)
            length = len(value)
            t = '0'*(8-length)
            label_dict.update({label_inst: t+value})

            if(input_list[i][1] in op_code):
                if(input_list[i][1]=='add' and len_inst==5):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code and input_list[i][4] in reg_code):
                        not_final.append(op_code['add']+'00' + reg_code[input_list[i][2]] + reg_code[input_list[i][3]] + reg_code[input_list[i][4]])
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
                        # error handling for wrong input
                        
                elif(input_list[i][1]=='sub' and len_inst==5):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code and input_list[i][4] in reg_code):
                        not_final.append(op_code['sub']+'00' + reg_code[input_list[i][2]] + reg_code[input_list[i][3]] + reg_code[input_list[i][4]])
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                elif(input_list[i][1]=='mul' and len_inst==5):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code and input_list[i][4] in reg_code):
                        not_final.append(op_code['mul']+'00' + reg_code[input_list[i][2]] + reg_code[input_list[i][3]] + reg_code[input_list[i][4]])
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                elif(input_list[i][1]=='xor' and len_inst==5):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code and input_list[i][4] in reg_code):
                        not_final.append(op_code['xor']+'00' + reg_code[input_list[i][2]] + reg_code[input_list[i][3]] + reg_code[input_list[i][4]])
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
                        i+=1

                elif(input_list[i][1]=='or' and len_inst==5):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code and input_list[i][4] in reg_code):
                        not_final.append(op_code['or']+'00' + reg_code[input_list[i][2]] + reg_code[input_list[i][3]] + reg_code[input_list[i][4]])

                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                elif(input_list[i][1]=='and' and len_inst==5):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code and input_list[i][4] in reg_code):
                        not_final.append(op_code['and']+'00' + reg_code[input_list[i][2]] + reg_code[input_list[i][3]] + reg_code[input_list[i][4]])
                    else:
                        error_list.append("ERROR!Register format incorrect." + "-" + "Line " + str(i))

                # Type B:
                elif(input_list[i][1]=='mov' and len_inst==4):
                    if(input_list[i][2] in reg_code):
                        movInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))
                
                elif(input_list[i][0]=='ls' and len_inst==4):
                    if(input_list[i][2] in reg_code):
                        lsInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                elif(input_list[i][0]=='rs' and len_inst==4):
                    if(input_list[i][2] in reg_code):
                        rsInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                # Type C:
                elif(input_list[i][1]=='div' and len_inst==4):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        divInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))         

                elif(input_list[i][0]=='not' and len_inst==4):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        not_final.append(op_code['not']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                elif(input_list[i][0]=='cmp' and len_inst==4):
                    if(input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        cmpInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+str(i))

                else:
                    error_list.append("Syntax Error. Line "+str(i))
            else:
                error_list.append("Illegal use of label. Line "+str(i))
        i+=1

    else:
        error_list.append("General Syntax Error. Line "+str(i))
        i+=1

r = 0
out=sys.stdout
if (len(error_list)>0):
    for r in range(len(error_list)):
        out.write(error_list[r]+"\n")
        sys.exit()
else:
    for r in range(len(final_print)):
        out.write(final_print[r]+"\n")