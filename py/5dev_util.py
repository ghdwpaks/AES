from os import rename
from Funs import tr
import copy as c
l1 = ["d4","df","5d","30"]
l2 = [
    ["02","03","01","01"],
    ["01","02","03","01"],
    ["01","01","02","03"],
    ["03","01","01","02"]
]

print(l1)
res = c.deepcopy(l1)
for i in range(len(l2)) :
    res = tr.XOR_list(l2[i],res)
print(res)