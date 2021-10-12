from os import popen, rename
from ENC.py import Funs

def ReturnUpSbox() :
        sbox = """63	7c	77	7b	f2	6b	6f	c5	30	01	67	2b	fe	d7	ab	76
        ca	82	c9	7d	fa	59	47	f0	ad	d4	a2	af	9c	a4	72	c0
        b7	fd	93	26	36	3f	f7	cc	34	a5	e5	f1	71	d8	31	15
        04	c7	23	c3	18	96	05	9a	07	12	80	e2	eb	27	b2	75
        09	83	2c	1a	1b	6e	5a	a0	52	3b	d6	b3	29	e3	2f	84
        53	d1	00	ed	20	fc	b1	5b	6a	cb	be	39	4a	4c	58	cf
        d0	ef	aa	fb	43	4d	33	85	45	f9	02	7f	50	3c	9f	a8
        51	a3	40	8f	92	9d	38	f5	bc	b6	da	21	10	ff	f3	d2
        cd	0c	13	ec	5f	97	44	17	c4	a7	7e	3d	64	5d	19	73
        60	81	4f	dc	22	2a	90	88	46	ee	b8	14	de	5e	0b	db
        e0	32	3a	0a	49	06	24	5c	c2	d3	ac	62	91	95	e4	79
        e7	c8	37	6d	8d	d5	4e	a9	6c	56	f4	ea	65	7a	ae	08
        ba	78	25	2e	1c	a6	b4	c6	e8	dd	74	1f	4b	bd	8b	8a
        70	3e	b5	66	48	03	f6	0e	61	35	57	b9	86	c1	1d	9e
        e1	f8	98	11	69	d9	8e	94	9b	1e	87	e9	ce	55	28	df
        8c	a1	89	0d	bf	e6	42	68	41	99	2d	0f	b0	54	bb	16"""
        sbox_list = sbox.split("\n")
        for i in range(len(sbox_list)) :
            sbox_list[i] = sbox_list[i].strip()
            sbox_list[i] = sbox_list[i].split("\t")
        return sbox_list

def ReturnUpRcon() :
    Rcon = []
    for i in range(0,8) :
        Rcon.append(Funs.tr.FillUp0(str(hex(2**i))[2:],2))
    return Rcon

def ApplyKey(sbox,key_part) :
    #key_part = '2b'
    key_part = list(key_part)
    res = []
    res.append(sbox[int(Funs.tr.str_int(key_part[0]))][int(Funs.tr.str_int(key_part[1]))])
    return res

def SetUpAllKey(sbox,key_list) :
    #key_list = "['2b', '28', 'ab', '09', '7e', 'ae', 'f7', 'cf', '15', 'd2', '15', '4f', '16', 'a6', '88', '3c']"
    res = []
    #print("key_list :",key_list)
    for i in key_list :
        res.extend(ApplyKey(sbox,i))
    #print("before res of list chunck :",res)
    res = Funs.tr.list_chunk(res,4)
    
    return res

def rot(key_part,rot=1) :
    #key_part = ['01', '8a', '84', 'eb']
    #res = ['8a', '84', 'eb', '01']
    #print("rot_3_1 key_part key_part :",key_part)
    res = []
    temp = []
    #for i in range(rot) :
    for i2 in range(4-rot) :
        res.append(key_part[i2+rot])
    
    for i3 in range(rot) :
        temp.append(key_part[i3])

    
    res.extend(temp)

    #print("rot_3_1 key_part res :",res)
    return res
    


def GetKey(path="key_folder/Key.txt",div=2) :
    f = open(path,"r")
    ls = f.readlines()
    f.close()
    str_key = str("".join(ls))
    key_list = []
    for i in range(0,len(str_key),div) :
        temp = str_key[i]
        for j in range(1,div) :
            temp += str_key[i+j]
        key_list.append(temp)
    return key_list

def ks_main(key_path) :

    sbox = ReturnUpSbox()
    rcons = ReturnUpRcon()
    rcons += ['1b','36'] 
    C_key = GetKey(key_path)
    #print("ENC.py KeyScheduling key_path :",key_path)
    #print("ENC.py KeyScheduling C_key :",C_key)
    C_key = Funs.tr.list_chunk(C_key,4)

    r = []
    #print("rcons :",rcons)
    for j in range(10) :
        rj = []
        tc = C_key  #target c key
        #print("j+1 :",j+1)
        if not j == 0 :
            tc = r[j-1]

        for i in range(len(tc)) :
            if i == 0 :
                #print("true")
                #r1tt = rot_3_1(r1t[len(r1t)-1-i])
                #print("SetUpAllKey(tc[3])[0]) :",SetUpAllKey(tc[3])[0])
                r1tt = rot(SetUpAllKey(sbox,tc[3])[0])
                #print("i :",i)
                #print("tc[i] :",tc[i])
                #print("r1tt :",r1tt)
                rcon = [rcons[j],'00','00','00']
                #print("rcon :",rcon)
                #print("rcon :",rcon)
                temp = Funs.tr.XOR_list(tc[i],r1tt)
                #print("temp 1 :",temp)
                temp = Funs.tr.XOR_list(temp,rcon)
                #print("temp 2 :",temp)
                rj.append(temp)
            else :
                #print("false")
                rj.append(Funs.tr.XOR_list(tc[i],rj[i-1]))
        #print("rj :")
        #print(Funs.#print_funcs.#print_list_nicly(rj))
        r.append(rj)
            

        #print("\t\ti = {} , temp : {}".format(i,temp))
    #Funs.#print_funcs.#print_list_nicly(r)
    return r

