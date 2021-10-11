import copy as c
from os import stat
import KeyScheduling as ks
from Funs import tr 
from Funs import print_funcs as p
ks.ks_main()
sbox = ks.ReturnUpSbox()
rcon = ks.ReturnUpRcon()
rkey = ks.ks_main()




def ShiftRows(state) :
    ShiftRows_state = tr.Vertical2Horizontal(state)
    
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

    res = tr.Horizontal2Vertical(ShiftRows_state)
    
    #print("ShiftRows res :",res)
    return res



def MixColumns(state) :
    
    for i in range(len(state)) :
        for j in range(len(state[i])) :
            state[i][j] = int("0x"+state[i][j],16)
    #print(state)


    state = tr.Vertical2Horizontal(state)
    #for (i = 0; i < 4; i++)
    for i in range(4) :
        t = state[0][i];

        Tmp = state[0][i] ^ state[1][i] ^ state[2][i] ^ state[3][i];

        Tm = state[0][i] ^ state[1][i]; Tm = tr.xtime(Tm); state[0][i] = state[0][i] ^ (Tm ^ Tmp);
        Tm = state[1][i] ^ state[2][i]; Tm = tr.xtime(Tm); state[1][i] ^= Tm ^ Tmp;
        Tm = state[2][i] ^ state[3][i]; Tm = tr.xtime(Tm); state[2][i] ^= Tm ^ Tmp;
        Tm = state[3][i] ^ t; Tm = tr.xtime(Tm); state[3][i] ^= Tm ^ Tmp;

    #print("state :",state)
    
    #print("state 1 :",state)
    for i in range(len(state)) :
        for j in range(len(state[i])) :
            state[i][j] = str(hex(state[i][j]))[2:]
            if (len(state[i][j])>2) :
                state[i][j] = state[i][j][1:]
            state[i][j] = tr.FillUp0(state[i][j],2)

    res = tr.Horizontal2Vertical(state)
    return res
    
def AddRoundKey(state,rkey,round_count) :
    res = []
    for i in range(len(state)) :
        res.append(tr.XOR_list(state[i],rkey[round_count][i]))
    return res






state = tr.SubBytes(ks.GetKey("key_folder/State_code.txt"),sbox)
print("state 1 :",state)

state = ShiftRows(state)
print("state 2 :",state)
state = MixColumns(state)
print("state 3 :",state)
state = AddRoundKey(state,rkey,0)
print("state 4 :",state)








