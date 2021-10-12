def rot(key_part,rot=1) :
    #key_part = ['8a', '84', 'eb', '01']
    #res = ['01', '8a', '84', 'eb']
    #print("rot_3_1 key_part key_part :",key_part)
    res = []
    temp = []
    for i in range(rot) :
        res.append(key_part[-(i+1)])

    for i in range(4-rot) :
        temp.append(key_part[i])
    
    res.extend(temp)


    #print("rot_3_1 key_part res :",res)
    return res

print(rot(['a', 'b', 'c', 'f']))
print(rot(['8a', '84', 'eb', '01']))


