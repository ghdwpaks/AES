def xtime(x) : 
    print("x :",x)
    print("x :",bin(x))
    a = x<<1
    print("a 1:",a)
    print("a 1:",bin(a))
    b = x>>7
    print("b 1:",b)
    print("b 1:",bin(b))
    b = b & 1
    print("b 2:",b)
    print("b 2:",bin(b))
    b = b * 0x1b
    print("b 3:",b)
    print("b 3:",bin(b))
    res = a ^ b
    print("res :",res)
    print("res :",bin(res))
    return res

    #return ((x<<1) ^ ( ( (x>>7) & 1 ) * 0x1b ))

def xtime2(x) : 
    print("x :",x)
    print("x :",bin(x))
    a = x>>1
    print("a :",a)
    print("a :",bin(a))
    b = x>>8
    print("b 1 :",b)
    print("b 1 :",bin(b))
    b = b&1
    print("b 2 :",b)
    print("b 2 :",bin(b))
    b = b*0x1f
    print("b 3 :",b)
    print("b 3 :",bin(b))
    res = a^b

    return res
def xtime2(x) : a = x>>1;b = x>>8;b = b&1;b = b*0x1f;res = a^b;return res
#1b : 27 : 0001 1011

#214 = xtime(107)
#107 = xtime2(214)
print("1"*500)
print(xtime2(247))
print("2"*500)
print(xtime2(214))





