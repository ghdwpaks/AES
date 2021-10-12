from DEC import enc_KeyScheduling as eks
from DEC.Funs import tr

def reSubBytes(state) :
    sbox = eks.ReturnUpSbox()
    #print("SubBytes state :",state)
    #state = [['d4', '27', '11', 'ae'], ['e0', 'df', '98', 'f1'], ['b8', 'b4', '5d', 'e5'], ['1e', '41', '52', '30']]
    temp = []
    for i in range(len(state)) :
        temp.extend(state[i])
    print("reSubBytes temp :",temp)
    res = []
    for i in range(len(temp)) :
        res.append(tr.RollBack_apply(temp[i],sbox))
    print("res :",res)
    return res



state = [['d4','27','11','ae'],['e0','bf','98','f1'],['b8','b4','5d','e5'],['1e','41','52','30']]
print(state)
reSubBytes(state)