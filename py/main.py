import copy as c
import KeyScheduling as ks
from Funs import tr as t
from Funs import print_funcs as p
ks.ks_main()
sbox = ks.ReturnUpSbox()
rcon = ks.ReturnUpRcon()
rkey = ks.ks_main()

def SubBytes(state,sbox) :
    state = ks.SetUpAllKey(sbox,state)
    state = t.list_chunk(state,4)[0]
    return state

def Vertical2Horizontal(state) :
    #세로와 가로
    ShiftRow_state_temp = []
    for i in range(len(state)) :
        ShiftRow_state_temp.extend(state[i])
    #print("ShiftRows ShiftRow_state_temp :",ShiftRow_state_temp)

    ShiftRows_state = []
    for i in range(4) :
        ShiftRows_state.append([])
        for j in range(4) :
            ShiftRows_state[i].append(ShiftRow_state_temp[(j*4)+i])
    return ShiftRows_state

def ShiftRows(state) :
    ShiftRow_state_temp = []
    for i in range(len(state)) :
        ShiftRow_state_temp.extend(state[i])
    #print("ShiftRows ShiftRow_state_temp :",ShiftRow_state_temp)

    ShiftRows_state = []
    for i in range(4) :
        ShiftRows_state.append([])
        for j in range(4) :
            ShiftRows_state[i].append(ShiftRow_state_temp[(j*4)+i])
    
    #print("\n\nshiftrows_state 1:",end="")
    #p.print_str_div(ShiftRows_state,1)

    
    #print("\n\n")
    for i in range(4) :
        #print("shiftrows state[",i,"] :",ShiftRows_state[i])
        temp = ks.rot(ShiftRows_state[i],i)
        #print("shiftrows temp",i,":",temp)
        #ShiftRows_state[i] = ks.rot(ShiftRows_state[i],i)
        ShiftRows_state[i] = temp
        #print("\n")
    #print("\n")
    
    #print("\n\nshiftrows_state 2:",end="")
    #p.print_str_div(ShiftRows_state,1)
    #print("\n\nshiftrows_state 3:",ShiftRows_state)
    #print("\n\n")

    res = []
    
    for i in range(4) :
        res.append([])
        for j in range(4) :
            res[i].append(ShiftRows_state[j][i])
    #print("ShiftRows res :",res)
    return res

def xtime(x) :
    return ((x<<1) ^ (((x>>7) & 1) * 0x1b))

def MixColumns(state) :
    
    for i in range(len(state)) :
        for j in range(len(state[i])) :
            state[i][j] = int("0x"+state[i][j],16)
    print(state)
    ShiftRow_state_temp = []
    for i in range(len(state)) :
        ShiftRow_state_temp.extend(state[i])
    ShiftRows_state = []
    for i in range(4) :
        ShiftRows_state.append([])
        for j in range(4) :
            ShiftRows_state[i].append(ShiftRow_state_temp[(j*4)+i])
    print("ShiftRows_state :",ShiftRows_state)

    state = c.deepcopy(ShiftRows_state)
    #for (i = 0; i < 4; i++)
    for i in range(4) :
        t = state[0][i];

        Tmp = state[0][i] ^ state[1][i] ^ state[2][i] ^ state[3][i];



        Tm = state[0][i] ^ state[1][i];
        Tm = xtime(Tm); 
        state[0][i] = state[0][i] ^ (Tm ^ Tmp);



        Tm = state[1][i] ^ state[2][i];
        Tm = xtime(Tm); 
        state[1][i] ^= Tm ^ Tmp;



        Tm = state[2][i] ^ state[3][i]; 
        Tm = xtime(Tm); 
        state[2][i] ^= Tm ^ Tmp;



        Tm = state[3][i] ^ t; 
        Tm = xtime(Tm); 
        state[3][i] ^= Tm ^ Tmp;
    print("state :",state)
    res = []
        
    for i in range(4) :
        res.append([])
        for j in range(4) :
            res[i].append(state[j][i])
    print("res 1 :",res)
    for i in range(len(res)) :
        for j in range(len(res[i])) :
            res[i][j] = str(hex(res[i][j]))[2:]
            if (len(res[i][j])>2) :
                res[i][j] = res[i][j][1:]
    print("res 2 :",res)
    




state = SubBytes(ks.GetKey("key_folder/State_code.txt"),sbox)
print("state 1 :",state)

state = ShiftRows(state)
print("state 2 :",state)
print("\n\n\n")
MixColumns(state)







