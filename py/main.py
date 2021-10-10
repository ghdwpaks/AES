from os import stat
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



def MixColumns(state) :
    pass
    




state = SubBytes(ks.GetKey("key_folder/State_code.txt"),sbox)
print("state 1 :",state)

state = ShiftRows(state)
print("state 2 :",state)








