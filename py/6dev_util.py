from os import rename
from Funs import tr
import KeyScheduling as k

mclt = k.GetKey("key_folder/mixcolumns_list.txt",1)
print("mclt :",mclt)
mcl = []
for i in range(len(mclt)) :
    mcl.append("0"+mclt[i])

mcl = tr.list_chunk(mcl,4)
print("mcl :",mcl)
    
l1 = ['d4', 'df', '5d', '30']


tr.hexstr_to_bin(l1[0])


