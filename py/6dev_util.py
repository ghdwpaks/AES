from os import rename
from Funs import tr
import KeyScheduling as k
def hexstr_to_bin(s,hexlist) :
    #s = "d4"

    


    s = list(s)
    for i in range(len(s)) :
        s[i] = tr.str_int(s[i],2)
    s.reverse()
    print("str ot hex s :",s)
    res = 0
    for i in range(len(s)) :
        res += s[i]*hexlist[i]
    print("res :",res)
    if res >= 256 :
        res -= 256
    



    
    
    

hexlist = [1]
temp = 0
for i in range(1,5) :
    hexlist.append(16**i)
print("hexlist :",hexlist)

    
l1 = ['d4', 'df', '5d', '30']


hexstr_to_bin(l1[0],hexlist)


