from os import rename
import copy as c

def xtime(x) :
    return ((x<<1) ^ (((x>>7) & 1) * 0x1b))

print(xtime(0x18))
state = [['d4', 'bf', '5d', '30'], ['e0', 'b4', '52', 'ae'], ['b8', '41', '11', 'f1'], ['1e', '27', '98', 'e5']]
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






