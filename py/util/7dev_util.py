from os import terminal_size
from Funs import tr 
def int_to_bin(inp) :
    #inp = 572
    #inp is int
    res = []
    #while True :
    hexlist = [1]
    temp = 0
    for i in range(1,5) :
        hexlist.append(16**i)
    hexlist.reverse()
    print(hexlist)
    res_len = 0
    for i in range(len(hexlist)) :
        #print("i :",i)
        #print("hexlist[i] :",hexlist[i])
        #print("res.append(inp//hexlist[i]) :",inp//hexlist[i])
        res_len += 1
        if i == len(hexlist)-1 :
            #print(False)
            res.append(inp)
        else :
            #print(True)
            appending = inp//hexlist[i]
            res.append(appending)
            if appending > 0 :
                inp -= hexlist[i]*appending
                
        #print("i :",i,"inp :",inp)
        #print("\n")
    
    #print("res_len :",res_len) 
    #print("res 1:",res)
    #print("inp :",inp)
    i = 0
    canpass = True
    while True :
        #print("i :",i)
        #print("res :",res)
        #print("len(res) :",len(res))
        if i > len(res)-1 :
            break

        if (res[i] == 0 or res[i] == "0" ) and canpass:
            res = res[1:]
        else :
            canpass = False
            
            #print("res[",i,"] :",res[i])
            #print("bin(res[i])) :",bin(res[i]))
            #print("str(bin(res[i]))[2:] :", str(bin(res[i]))[2:])
            
            res[i] = tr.FillUp0(str(bin(res[i]))[2:])
            i+=1
        #print("\n\n")
        
        
    res = "".join(res)
    
    #print("res 2:",res)
    #res = "001000111100"
    return res

#print(int_to_bin(572))
while True :
    i = int(input("입력 :"))
    print(int_to_bin(i))
