#from DEC.enc_KeyScheduling import 
#from DEC.Funs import tr
from os import stat


def FillUp0(i,byte=4) :
        #i = 10
        i = list(i)
        while True :
            if len(i) < byte :
                i.insert(0,"0")
            else :
                break
        return "".join(i)
def Vertical2Horizontal(state) :
    #세로를 가로로
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



def Horizontal2Vertical(state) :
    #가로를 세로로
    res = []
    for i in range(4) :
        res.append([])
        for j in range(4) :
            res[i].append(state[j][i])
    return res

def xtime(x) : return ((x<<1) ^ (((x>>7) & 1) * 0x1b))
def dev(state) :
    for i in range(4) :

        t = state[0][i]

        Tmp = state[0][i] ^ state[1][i] ^ state[2][i] ^ state[3][i]

        Tm = state[0][i] ^ state[1][i]


        Tm = xtime(Tm)
        state[0][i] = state[0][i] ^ (Tm ^ Tmp)


        Tm = state[1][i] ^ state[2][i]
        Tm = xtime(Tm)
        state[1][i] ^= Tm ^ Tmp


        Tm = state[2][i] ^ state[3][i]
        Tm = xtime(Tm)
        state[2][i] ^= Tm ^ Tmp


        Tm = state[3][i] ^ t
        Tm = xtime(Tm)
        state[3][i] ^= Tm ^ Tmp


    for i in range(len(state)) :
        for j in range(len(state[i])) :
            state[i][j] = str(hex(state[i][j]))[2:]
            if (len(state[i][j])>2) :
                state[i][j] = state[i][j][1:]
            state[i][j] = FillUp0(state[i][j],2)

    res = Horizontal2Vertical(state)
    return res


state = [["04","66","81","e5"],["e0","cb","19","9a"],["48","f8","d3","7a"],["28","06","26","4c"]]
state = Vertical2Horizontal(state)
for i in range(len(state)) :
    for j in range(len(state[i])) :
        state[i][j] = int("0x"+state[i][j],16)
res = dev(state)
print(res)  


