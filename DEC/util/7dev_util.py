

def xtime2(x) : 
    a = x>>1
    b = x>>8
    b = b&1
    b = b*2
    res = a^b
    return res
def xtime(x) : 
    a = x<<1
    b = x>>7
    b = b & 1
    b = b * 0x1b
    res = a ^ b
    return res

'''
for j in range(50) :
    print("j :",j)
    print("\n")
'''

def xtime2(x) : a = x>>1;b = x>>8;b = b&1;b = b*2;res = a^b;return res

for i in range(172) :
    if not xtime(i) == xtime(xtime2(xtime(i))) :
        print(i,"\t",xtime(i),"\t",xtime(xtime2(xtime(i))),"\t",(xtime(i)-xtime(xtime2(xtime(i)))))