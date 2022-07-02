l=[]
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
while(True):
    inp=list(map(str,input().split()))

    # Type A:
    if(inp[0]=='add'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            print(op_code['add']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
                # error handling for wrong input
    elif(inp[0]=='sub'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            print(op_code['sub']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])

    elif(inp[0]=='mul'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            print(op_code['mul']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])

    elif(inp[0]=='xor'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            print(op_code['xor']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
 
    elif(inp[0]=='or'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            print(op_code['or']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])
   
    elif(inp[0]=='and'):
        if(inp[1] in reg_code and inp[2] in reg_code and inp[3] in reg_code):
            print(op_code['and']+'00' + reg_code[inp[1]] + reg_code[inp[2]] + reg_code[inp[3]])

    # Type B:
    elif(inp[0]=='mov'):
        if(inp[1] in reg_code):
            word = inp[2]
            word_list = list(word)
            if(word_list[0]=='$'):
                word_list.remove('$')
                word_final = ''.join(word_list)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                print(op_code['mov'][1] + reg_code[inp[1]] + t + value)
            else:
                if(inp[2] in reg_code):  #Type C
                    print(op_code['mov'][2] + '00000' + reg_code[inp[1]] + reg_code[inp[2]] )
    
    elif(inp[0]=='ls'):
        if(inp[1] in reg_code):
            word = inp[2]
            word_list = list(word)
            if(word_list[0]=='$'):
                word_list.remove('$')
                word_final = ''.join(word_list)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                print(op_code['ls'] + reg_code[inp[1]] + t + value)

    elif(inp[0]=='rs'):
        if(inp[1] in reg_code):
            word = inp[2]
            word_list = list(word)
            if(word_list[0]=='$'):
                word_list.remove('$')
                word_final = ''.join(word_list)
                decimal_number = str(word_final)
                value = dec_to_bi(decimal_number)
                value  = str(value)
                length = len(value)
                t = '0'*(8-length)
                print(op_code['rs'] + reg_code[inp[1]] + t + value)                

    # Type C:
    elif(inp[0]=='div'):
        if(inp[1] in reg_code and inp[2] in reg_code):
            print(op_code['div']+'00000' + reg_code[inp[1]] + reg_code[inp[2]])            

    elif(inp[0]=='not'):
        if(inp[1] in reg_code and inp[2] in reg_code):
            print(op_code['not']+'00000' + reg_code[inp[1]] + reg_code[inp[2]])         

    elif(inp[0]=='cmp'):
        if(inp[1] in reg_code and inp[2] in reg_code):
            print(op_code['cmp']+'00000' + reg_code[inp[1]] + reg_code[inp[2]])         

    #Type D
    elif(inp[0]=='ld'):
        if(inp[1] in reg_code):
            print(op_code['ld'] + reg_code[inp[1]] + inp[2])     ######doubt

    elif(inp[0]=='st'):
        if(inp[1] in reg_code):
            print(op_code['st'] + reg_code[inp[1]] + inp[2])     ######doubt

    #Type E
    elif(inp[0]=='jmp'):
        print(op_code['jmp'] + inp[1])     ######doubt

    elif(inp[0]=='jlt'):
        print(op_code['jlt'] + inp[1])     ######doubt

    elif(inp[0]=='jgt'):
        print(op_code['jgt'] + inp[1])     ######doubt      

    elif(inp[0]=='je'):
        print(op_code['je'] + inp[1])     ######doubt   

    #Type F
    elif(inp[0]=='hlt'):
        print(op_code['hlt']+'00000000000')
        break
