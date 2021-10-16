def xtime(x) : return ((x<<1) ^ ( ( (x>>7) & 1 ) * 0x1b ))
state = [[212],[191],[93],[48]]


t = state[0][0]
Tmp = state[0][0] ^ state[1][0] ^ state[2][0] ^ state[3][0]

Tm = state[0][0] ^ state[1][0]
Tm = xtime(Tm)
state[0][0] ^= Tm ^ Tmp

Tm = state[1][0] ^ state[2][0]
Tm = xtime(Tm)
state[1][0] ^= Tm ^ Tmp

Tm = state[2][0] ^ state[3][0]
Tm = xtime(Tm)
state[2][0] ^= Tm ^ Tmp

Tm = state[3][0] ^ t
Tm = xtime(Tm)
state[3][0] = state[3][0]^(Tm ^ Tmp)

