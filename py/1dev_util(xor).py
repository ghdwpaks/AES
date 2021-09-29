def transport(n) :
    #n = "2b"
    res = []
    n = list(n)
    for i in n :

        if i.isalpha() : i = str_int(i)
        else : i = int(i)

        temp = list(bin(i))
        temp.pop(0)
        temp.pop(0)
        temp = FillUp0("".join(temp))
        res.append(temp)
    return "".join(res)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def retransport(s) :
    #s = "0001"

    s = list_chunk(list(FillUp0(str(s))),4)
    #print(s)
    r = []
    for j in range(len(s)) :
        t = 0
        for i in range(len(s[j])) :
            t += ((len(s[j])-i-1)**2)*((int(s[j][i])))
        r.append(str(str_int(t)))

    return "".join(r)
        
    

def str_int(s) :
    if s == "a" : return 10
    elif s == "b" : return 11
    elif s == "c" : return 12
    elif s == "d" : return 13
    elif s == "e" : return 14
    elif s == "f" : return 15
    elif s == "A" : return 10
    elif s == "B" : return 11
    elif s == "C" : return 12
    elif s == "D" : return 13
    elif s == "E" : return 14
    elif s == "F" : return 15
    elif s == 10 : return "a"
    elif s == 11 : return "b"
    elif s == 12 : return "c"
    elif s == 13 : return "d"
    elif s == 14 : return "e"
    elif s == 15 : return "f"
    else : return s

def FillUp0(i,byte=4) :
    #i = 10
    i = list(i)
    while True :
        if len(i) < byte :
            i.insert(0,"0")
        else :
            break
    return "".join(i)

def XorOnStr(s1,s2) :
    s1 = list(str(s1))
    s2 = list(str(s2))
    res = []
    for i in range((len(s1)+len(s2))//2) :
        if s1[i] == s2[i] : res.append("0")
        else : res.append("1")
    return "".join(res)



w1 = transport("2b")
w2 = transport("8a")
w3 = XorOnStr(w1,w2)
w4 = transport("01")
w5 = XorOnStr(w3,w4)
print(w5)
r6 = retransport(w5)
print(r6)

i1 = input("입력 : ")
print(transport(i1))
#transport는 정상적인데 retransport 부분의 0을 채우는 부분에서 문제가 있는거같아 보임(확인안됨)
print(retransport(transport(i1)))




