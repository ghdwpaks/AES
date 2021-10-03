from os import rename
from Funs import tr
import KeyScheduling as k



hexlist = [1]
temp = 0
for i in range(1,5) :
    hexlist.append(16**i)
print("hexlist :",hexlist)

    
l1 = ['d4', 'df', '5d', '30']


tr.hexstr_to_bin(l1[0])


