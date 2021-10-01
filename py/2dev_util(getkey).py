import Funs


#2b28ab097eaef7cf15d2154f16a6883c

f = open("Key.txt","r")
ls = f.readlines()
f.close()
str_key = str("".join(ls))
key_list = []
for i in range(0,len(str_key),2) :
    key_list.append(str_key[i]+str_key[i+1])
print(key_list)

enc_key_list = []
for i in key_list :
    enc_key_list.append(Funs.tr.transport(i))
print(enc_key_list)

dec_key_list = []
for i in enc_key_list :
    dec_key_list.append(Funs.tr.retransport(i))
print(dec_key_list)