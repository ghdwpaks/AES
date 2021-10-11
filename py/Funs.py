from os import rename
import copy as c
import KeyScheduling as ks

class tr :
    def xtime(x) : return ((x<<1) ^ (((x>>7) & 1) * 0x1b))
    
    def Vertical2Horizontal(state) :
        #세로를 가로로
        ShiftRow_state_temp = []
        for i in range(len(state)) :
            ShiftRow_state_temp.extend(state[i])
        #print("ShiftRows ShiftRow_state_temp :",ShiftRow_state_temp)

        ShiftRows_state = []
        for i in range(4) :
            ShiftRows_state.append([])
            for j in range(4) :
                ShiftRows_state[i].append(ShiftRow_state_temp[(j*4)+i])
        return ShiftRows_state

    def Horizontal2Vertical(state) :
        #가로를 세로로
        res = []
        for i in range(4) :
            res.append([])
            for j in range(4) :
                res[i].append(state[j][i])
        return res

    def transport(n) :
        #n = "2b"
        res = []
        n = list(n)
        for i in n :

            if i.isalpha() : i = tr.str_int(i)
            else : i = int(i)

            temp = list(bin(i))
            temp.pop(0)
            temp.pop(0)
            temp = tr.FillUp0("".join(temp))
            temp = tr.str_int("".join(temp))

            res.append(temp) 
            #print("tr transport temp :",temp)
        return "".join(res)

    def list_chunk(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]

    def retransport(s) :
        if type(s) == type([]) :
            s = "".join(s)
        #s = "0001"

        s = tr.list_chunk(list(tr.FillUp0(str(s))),4)
        #print("retransport s :",s)
        r = []
        for j in range(len(s)) :
            t = 0
            for i in range(len(s[j])) :
                #print("len(s[j])-i-1 :",len(s[j])-i-1)
                #print("(2**(len(s[j])-i-1)) :",(2**(len(s[j])-i-1)))
                #print("(int(s[j][i])) :",(int(s[j][i])))
                #print("t += :",(2**(len(s[j])-i-1))*(int(s[j][i])))
                t += ((2**(len(s[j])-i-1))*(int(s[j][i])))
                #print("\n")
            r.append(str(tr.str_int(t)))
            #print("\n")
        

        return "".join(r)
    def hexstr_to_int(s) :
        hexlist = [1]
        temp = 0
        for i in range(1,5) :
            hexlist.append(16**i)
        #print("hexlist :",hexlist)
        #s = "d4"
        s = list(s)
        for i in range(len(s)) :
            s[i] = tr.str_int(s[i],2)
        s.reverse()
        #print("str ot hex s :",s)
        res = 0
        for i in range(len(s)) :
            res += s[i]*hexlist[i]
        #print("res :",res)
        return res 
    
    def int_to_bin(inp) :
        res = []
        hexlist = [1]
        temp = 0
        for i in range(1,5) :
            hexlist.append(16**i)
        hexlist.reverse()
        print(hexlist)
        res_len = 0
        for i in range(len(hexlist)) :
            res_len += 1
            if i == len(hexlist)-1 : res.append(inp)
            else :
                appending = inp//hexlist[i]
                res.append(appending)
                if appending > 0 :
                    inp -= hexlist[i]*appending
        i = 0
        canpass = True
        while True :
            if i > len(res)-1 : break
            if (res[i] == 0 or res[i] == "0" ) and canpass: res = res[1:]
            else :
                canpass = False
                res[i] = tr.FillUp0(str(bin(res[i]))[2:])
                i+=1
            
            
        res = "".join(res)
        return res
    
        

    def str_int(s,type=1) :
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
        elif s == "10" : return "a"
        elif s == "11" : return "b"
        elif s == "12" : return "c"
        elif s == "13" : return "d"
        elif s == "14" : return "e"
        elif s == "15" : return "f"
        elif s == 10 : return "a"
        elif s == 11 : return "b"
        elif s == 12 : return "c"
        elif s == 13 : return "d"
        elif s == 14 : return "e"
        elif s == 15 : return "f"
        else : 
            if type == 1 :
                return s
            elif type == 2 :
                return int(s)
    
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
        #s1 데이터 추정 : "00101010"
        #s2 데이터 추정 : "01100110"
        #print("funs tr XorOnStr s1 :",s1)
        #print("funs tr XorOnStr s2 :",s2)
        if not len(s1) == len(s2) :
            if len(s1) > len(s2) :
                s2 = tr.FillUp0(s2,len(s1))
            else :
                s1 = tr.FillUp0(s1,len(s2))
        s1 = list(str(s1))
        s2 = list(str(s2))
        res = []
        for i in range((len(s1)+len(s2))//2) :
            if s1[i] == s2[i] : res.append("0")
            else : res.append("1")
        return "".join(res)

    def XOR_list(l1,l2) :
        #l1 = ['f3', '59', '47', 'f1']
        #l2 = ['09', 'cf', '4f', '3c']
        
        #print("funs tr xor word l1 :",l1)
        #print("funs tr xor word l2 :",l2)
        res = []
        for i in range((len(l1)+len(l2))//2) :
            t1 = tr.transport(l1[i])
            t2 = tr.transport(l2[i])
            res.append(tr.retransport(tr.XorOnStr(t1,t2)))
        return res
class print_funcs :
    

    def print_str_div(prints,div_num=0) :
        #div num 은 몇번 출력 당 줄을 넘을건지 미리 알려주는 변수.
        for i in range(len(prints)) :
            if i % div_num == 0 :
                print()
            print(prints[i],end="")
        
        
    def print_list_nicly(arr) :
        arr = str(arr)
        for i in range(len(arr)) :
            if arr[i-1] == "]" and arr[i] == "," :
                print()
            print(arr[i],end="")
        print()


