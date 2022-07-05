input_list = []
final_print = []
var_dict = {}
i = 0
var_count = 0
k=0
p=0

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

while(True):
    inp=list(map(str,input().split()))
    input_list.append(inp)
    if('hlt' in inp):
        break

len_list = len(input_list)

for p in range(len_list):
    if(input_list[p][0]=='var'):
        var_count+=1
    elif(input_list[p][0] in op_code):
        k = p
        break

for p in range(k+1, len_list):
    if(input_list[p][0]=='var'):
        print("Error")
        quit()

if(input_list[len_list-1][0] != 'hlt'):
    print("Error")

s = 0
for h in range(len_list):
    if(input_list[h][0] == 'hlt'):
        s = 1

if (s == 0):
    print("Missing halt")
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
            error_list.append("Immediate value invalid. Line "+i)
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
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

def lsInst():
    word = input_list[i][2]
    word_list = list(word)
    if(word_list[0]=='$'):
        word_list.remove('$')
        word_final = ''.join(word_list)
        if (int(word_final)>255 or int(word_final)<0):
            error_list.append("Immediate value invalid. Line "+i)
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
            error_list.append("Immediate value invalid. Line "+i)
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

#to store value in 16- bit register

for i in range(len_list):
    # Type A:
    if(input_list[i][0]=='add'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            print(addInst())
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1
            # error handling for wrong input
            
    elif(input_list[i][0]=='sub'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            subInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    elif(input_list[i][0]=='mul'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            mulInst()
            i=i+1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i=i+1

    elif(input_list[i][0]=='xor'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            xorInst()
            i = i + 1

        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    elif(input_list[i][0]=='or'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            orInst()
            i = i + 1

        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    elif(input_list[i][0]=='and'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
            andInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    # Type B:
    elif(input_list[i][0]=='mov'):
        if(input_list[i][1] in reg_code):
            movInst()
            i=i+1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1
    
    elif(input_list[i][0]=='ls'):
        if(input_list[i][1] in reg_code):
            lsInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    elif(input_list[i][0]=='rs'):
        if(input_list[i][1] in reg_code):
            rsInst()
            i+=1         
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    # Type C:
    elif(input_list[i][0]=='div'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
            divInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)         
            i+=1

    elif(input_list[i][0]=='not'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
            final_print.append(op_code['not']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])
            i=i+1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i=i+1      

    elif(input_list[i][0]=='cmp'):
        if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
            cmpInst()
            i+=1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    #Type D
    elif(input_list[i][0]=='ld'):
        if(input_list[i][1] in reg_code):
            if(input_list[i][2] in var_list):
                final_print.append(op_code['ld'] + reg_code[input_list[i][1]] + var_dict[input_list[i][2]])     ######doubt
                i+=1
            else:
                error_list.append("Error! Variable not defined!"+"-"+"Line "+i)
                i=i+1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    elif(input_list[i][0]=='st'):
        if(input_list[i][1] in reg_code):
            if(input_list[i][2] in var_list):
                final_print.append(op_code['st'] + reg_code[input_list[i][1]] + var_dict[input_list[i][2]])     ######doubt
                i+=1
            else:
                error_list.append("Error! Variable not defined!"+"-"+"Line "+i)
                i=i+1
        else:
            error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
            i+=1

    #Type E
    elif(input_list[i][0]=='jmp'):
        final_print.append(op_code['jmp'] + '000' + value)     ######doubt
        i+=1

    elif(input_list[i][0]=='jlt'):
        final_print.append(op_code['jlt'] + '000' + value)     ######doubt
        i+=1

    elif(input_list[i][0]=='jgt'):
        final_print.append(op_code['jgt'] + '000' +  value)     ######doubt      
        i+=1

    elif(input_list[i][0]=='je'):
        final_print.append(op_code['je'] + '000' + value)     ######doubt   
        i=i+1

    #Type F
    elif(input_list[i][0]=='hlt'):
        final_print.append(op_code['hlt']+'00000000000')
        i+=1
        if(i==len_list):
            break

    elif(input_list[i][0]=='var'):
        # q=0
        var_list. append(input_list[i][1])
        q = var_list.index(input_list[i][1])
        print(len_list)
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
            print("Illegal label name")
            quit()
        else:
            if(input_list[i][1] in op_code):
                if(input_list[i][0]=='add'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        addInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
                        # error handling for wrong input
                        
                elif(input_list[i][0]=='sub'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        subInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                elif(input_list[i][0]=='mul'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        mulInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                elif(input_list[i][0]=='xor'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        xorInst()

                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
                        i+=1

                elif(input_list[i][0]=='or'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        orInst()

                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                elif(input_list[i][0]=='and'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code and input_list[i][3] in reg_code):
                        andInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                # Type B:
                elif(input_list[i][0]=='mov'):
                    if(input_list[i][1] in reg_code):
                        movInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)
                
                elif(input_list[i][0]=='ls'):
                    if(input_list[i][1] in reg_code):
                        lsInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                elif(input_list[i][0]=='rs'):
                    if(input_list[i][1] in reg_code):
                        rsInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                # Type C:
                elif(input_list[i][0]=='div'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
                        divInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)         

                elif(input_list[i][0]=='not'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
                        final_print.append(op_code['not']+'00000' + reg_code[input_list[i][1]] + reg_code[input_list[i][2]])
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

                elif(input_list[i][0]=='cmp'):
                    if(input_list[i][1] in reg_code and input_list[i][2] in reg_code):
                        cmpInst()
                    else:
                        error_list.append("ERROR!Register format incorrect."+"-"+"Line "+i)

            else:
                print("Illegal use of label")
                exit()
        i=i+1

    else:
        error_list.append("General Syntax Error.")
        i+=1

if (len(error_list)>0):
    print(error_list[0])
    #print(*error_list,sep='\n')

output = open('output.txt', 'w')
for k in final_print:
    output.writelines(k)

print(*final_print,sep='\n')
print(*var_list)
