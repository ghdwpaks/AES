from os import popen
import Funs

Rcon = []
for i in range(0,8) :
    t = str(hex(2**i))[2:]
    Rcon.append(Funs.tr.FillUp0(t,2))
Rcon = ("".join(Rcon))+"1b36"
print(Rcon)