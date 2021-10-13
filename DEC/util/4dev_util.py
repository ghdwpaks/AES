def xtime(x) : 
    return (
        (x<<1) ^ ( ( (x>>7) & 1 ) * 0x1b )
    )
for i in range(40) :
    print("xtime(",i,") :",xtime(i))
a = xtime(10)
print(a)
print("*"*500)
res = 0
for i in range(500) :
    if i*2 == xtime(i) :
        res += 1
    else :
        print("xtime(",i,") :",xtime(i),i*2,xtime(i)-(i*2))
print(res)
print("*"*500)

for i in range(10) :
    print((2**i),"\t",xtime(2**i),end="\t")
    if ((2**i)*2) == xtime(2**i) :
        print()
    else :
        print(xtime(2**i)-((2**i)*2))