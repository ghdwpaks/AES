def xtime(x) : return ((x<<1) ^ ( ( (x>>7) & 1 ) * 0x1b ))


print(xtime(98))