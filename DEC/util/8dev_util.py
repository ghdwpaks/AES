
def xtime2(x,hex1=2) : 
    a = x>>1
    b = x>>8
    b = b&1
    b = b*hex1
    res = a^b
    return res
def xtime(x) : 
    a = x<<1
    b = x>>7
    b = b & 1
    b = b * 0x1b
    res = a ^ b
    return res

def xtime3(x) : 
    a = x>>1
    b = x>>8
    b = b&1
    b = b*13
    res = a^b
    return res





state1 = [[212],[191],[93],[48]]
state2 = [[4], [102], [129], [229]]

tm1 = [107,84,249,57,226,109,228,230,252,78,80,224,73,191,125,251]
tm2 = [214,168,489,114,479,218,467,471,483,156,160,475,146,357,250,493]

for i in range(len(tm1)) :
    print(tm1[i],"\t",xtime2(tm2[i]))

print("\n\n\n")
for j in range(-50,100,1) :
    print("j :",j)
    for i in range(len(tm1)) :
        if not tm1[i] == xtime2(tm2[i],j) :
            print(tm1[i],"\t",xtime2(tm2[i],j),"\t",((tm1[i])-(xtime2(tm2[i],j))))
print("\n"*5)
for i in range(len(tm1)) :
    print(tm1[i],"\t",xtime3(tm2[i]),"\t",(tm1[i]-xtime3(tm2[i])))





