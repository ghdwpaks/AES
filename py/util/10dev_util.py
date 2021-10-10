import copy as c
a = 0x16
b = 0x17
print("type(a) :",type(a))
print(a^b)

state = [['d4', 'bf', '5d', '30'], ['e0', 'b4', '52', 'ae'], ['b8', '41', '11', 'f1'], ['1e', '27', '98', 'e5']]
#print("0x"+state[0][0])

for i in range(len(state)) :
    for j in range(len(state[i])) :
        print("type(hex(int('0x'+state[i][j],16))) :",type(hex(int("0x"+state[i][j],16))))
        state[i][j] = hex(int("0x"+state[i][j],16))

    
print(state)
print("state[0][0] :",state[0][0])
print("type(state[0][0]) :",type(state[0][0]))
print(type(state[0][0]) == type(0x16))


for i in range(len(str(state))) :
    if not str(state)[i] == "'" :
        print(str(state)[i],end="")
print("\n\n")
state = [[0xd4, 0xbf, 0x5d, 0x30], [0xe0, 0xb4, 0x52, 0xae], [0xb8, 0x41, 0x11, 0xf1], [0x1e, 0x27, 0x98, 0xe5]]
print("state :",state)

