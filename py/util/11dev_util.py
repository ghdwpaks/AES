state = ['d4', 'bf', '5d', '30']
for i in range(len(state)) :
    state[i] = int("0x"+state[i],16)
print(state)

state = [['d4', 'bf', '5d', '30'], ['e0', 'b4', '52', 'ae'], ['b8', '41', '11', 'f1'], ['1e', '27', '98', 'e5']]
for i in range(len(state)) :
    for j in range(len(state[i])) :
        state[i][j] = int("0x"+state[i][j],16)
print(state)