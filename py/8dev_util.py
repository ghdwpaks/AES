def XorOnStr(s1,s2) :
    #s1 데이터 추정 : "00101010"
    #s2 데이터 추정 : "01100110"
    #print("funs tr XorOnStr s1 :",s1)
    #print("funs tr XorOnStr s2 :",s2)
    if not len(s1) == len(s2) :
        print("entered")
        if len(s1) > len(s2) :
            s2 = FillUp0(s2,len(s1))
        else :
            s1 = FillUp0(s1,len(s2))
    s1 = list(str(s1))
    s2 = list(str(s2))
    res = []
    for i in range((len(s1)+len(s2))//2) :
        if s1[i] == s2[i] : res.append("0")
        else : res.append("1")
    return "".join(res)

    
def FillUp0(i,byte=4) :
    #i = 10
    i = list(i)
    while True :
        if len(i) < byte :
            i.insert(0,"0")
        else :
            break
    return "".join(i)

print(XorOnStr("100","1110000"))