from os import rename
from Funs import tr
import KeyScheduling as k
import main

def MixColumns_cal_list(l,mcl,loc) :
    print("\n")
    # l = ['d4', 'bf', '5d', '30']
    '''
      mcl = [['02', '03', '01', '01'], ['01', '02', '03', '01'], ['01', '01', '02', '03'], ['03', '01', '01', '02']]  
    '''
    res = []
    temp_res = tr.hexstr_to_int(l[0]) * int(mcl[loc][0])
    print("temp_res 1:",temp_res)
    for i in range(1,len(l)) :
        temp = tr.hexstr_to_int(l[i]) * int(mcl[loc][i])
        print("l[i] :",l[i])
        print("tr.hexstr_to_int(l[i]) :",tr.hexstr_to_int(l[i]))
        print("int(mcl[loc][i]) :",int(mcl[loc][i]))
        print("tr.hexstr_to_int(l[i]) * int(mcl[loc][i]) :",tr.hexstr_to_int(l[i]) * int(mcl[loc][i]))
        print("temp_res 2:",temp_res,"temp :",temp)
        if temp > 255 : 
            temp %= 256 
        temp_res = temp ^ temp_res
        print("temp_res 3:",temp_res)
        print("\n")
    print("MixColumns_cal_list temp_res 1:",temp_res)    
    if temp_res > 255 : 
        temp_res %= 256 
    print("MixColumns_cal_list temp_res 2:",temp_res)
    
mcl = main.setup_mcl()
l1 = ['d4', 'df', '5d', '30']
l2 = ["93","33","fc","82"]

MixColumns_cal_list(l1,mcl,0)


