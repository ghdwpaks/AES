def xtime(x) : return ((x<<1) ^ ( ( (x>>7) & 1 ) * 0x1b ))

state = [[212],[191],[93],[48]]
print("state :",state)
Tmp = state[0][0] ^ state[1][0] ^ state[2][0] ^ state[3][0]
print("Tmp :",Tmp)
t = state[0][0]
print("t :",t)
print("\n\n")

Tm = state[0][0] ^ state[1][0]
print("Tm 1:",Tm)
Tm = xtime(Tm)
print("Tm 2:",Tm)
state[0][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[3][0] :",state[3][0])
print("state :",state)
print("\n\n")

Tm = state[1][0] ^ state[2][0]
print("Tm 1:",Tm)
Tm = xtime(Tm)
print("Tm 2:",Tm)
state[1][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[2][0] :",state[2][0])
print("state :",state)
print("\n\n")

Tm = state[2][0] ^ state[3][0]
print("Tm 1:",Tm)
Tm = xtime(Tm)
print("Tm 2:",Tm)
state[2][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[1][0] :",state[1][0])
print("state :",state)
print("\n\n")

Tm = state[3][0] ^ t
print("Tm 1:",Tm)
Tm = xtime(Tm)
print("Tm 2:",Tm)
state[3][0] ^= Tm ^ Tmp
print("Tm ^ Tmp :",Tm ^ Tmp)
print("state[0][0] :",state[0][0])
print("state :",state)
print("\n\n")
print("state :",state)