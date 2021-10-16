#xtime3 from 8dev_util.py

def xtime3(x) : 
    a = x>>1
    b = x>>8
    b = b&1
    b = b*13
    res = a^b
    return res


state = [[4],[102],[129],[229]]

t = state[0][0]
Tmp = state[0][0] ^ state[1][0] ^ state[2][0] ^ state[3][0]

Tm = state[3][0] ^ t
Tm = xtime3(Tm)
state[3][0] ^= Tm ^ Tmp

Tm = state[2][0] ^ state[3][0]
Tm = xtime3(Tm)
state[2][0] ^= Tm ^ Tmp

Tm = state[1][0] ^ state[2][0]
Tm = xtime3(Tm)
state[1][0] ^= Tm ^ Tmp

Tm = state[0][0] ^ state[1][0]
Tm = xtime3(Tm)
state[0][0] ^= Tm ^ Tmp

print(state)
'''
입력수치 : [[4],[102],[129],[229]]
목표수치 : [[212],[191],[93],[48]]
결과수치 : [[10], [20], [142], [147]]
'''


state = [[4],[102],[129],[229]]

t = state[0][0]
Tmp = state[0][0] ^ state[1][0] ^ state[2][0] ^ state[3][0]

Tm = state[0][0] ^ state[1][0]
Tm = xtime3(Tm)
state[0][0] ^= Tm ^ Tmp

Tm = state[1][0] ^ state[2][0]
Tm = xtime3(Tm)
state[1][0] ^= Tm ^ Tmp

Tm = state[2][0] ^ state[3][0]
Tm = xtime3(Tm)
state[2][0] ^= Tm ^ Tmp

Tm = state[3][0] ^ t
Tm = xtime3(Tm)
state[3][0] ^= Tm ^ Tmp
print(state)

'''
입력수치 : [[4],[102],[129],[229]]
결과수치 : [[51],[19],[181],[147]]
목표수치 : [[212],[191],[93],[48]]
'''

state = [[4],[102],[129],[229]]
print("state :",state)

Tmp = state[0][0] ^ state[1][0] ^ state[2][0] ^ state[3][0]
print("Tmp :",Tmp)
t = state[3][0]
print("t :",t)
print("\n\n")
Tm = state[3][0] ^ state[2][0]
print("Tm 1:",Tm)
Tm = xtime3(Tm)
print("Tm 2:",Tm)
state[3][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[3][0] :",state[3][0])
print("state :",state)
print("\n\n")
Tm = state[2][0] ^ state[1][0]
print("Tm 1:",Tm)
Tm = xtime3(Tm)
print("Tm 2:",Tm)
state[2][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[2][0] :",state[2][0])
print("state :",state)
print("\n\n")
Tm = state[1][0] ^ state[0][0]
print("Tm 1:",Tm)
Tm = xtime3(Tm)
print("Tm 2:",Tm)
state[1][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[1][0] :",state[1][0])
print("state :",state)
print("\n\n")
Tm = state[0][0] ^ t
print("Tm 1:",Tm)
Tm = xtime3(Tm)
print("Tm 2:",Tm)
state[0][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[0][0] :",state[0][0])
print("state :",state)

print("\n\n",state)
'''
입력수치 : [[4],[102],[129],[229]]
결과수치 : [[4], [8], [182], [227]]
목표수치 : [[212],[191],[93],[48]]
'''

Tmp = state[0][0] ^ state[1][0] ^ state[2][0] ^ state[3][0]
t = state[3][0]


Tm = state[3][0] ^ state[2][0]
Tm = xtime3(Tm)
state[3][0] ^= Tm ^ Tmp


Tm = state[2][0] ^ state[1][0]
Tm = xtime3(Tm)
state[2][0] ^= Tm ^ Tmp


Tm = state[1][0] ^ state[0][0]
Tm = xtime3(Tm)
state[1][0] ^= Tm ^ Tmp


Tm = state[0][0] ^ t
Tm = xtime3(Tm)
state[0][0] ^= Tm ^ Tmp


00