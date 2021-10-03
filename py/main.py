from os import stat
import KeyScheduling as ks
from Funs import tr as t
from Funs import print_funcs as p
ks.ks_main()
sbox = ks.ReturnUpSbox()
rcon = ks.ReturnUpRcon()
rkey = ks.ks_main()

def SubBytes(state,sbox) :
    state = ks.SetUpAllKey(sbox,state)
    state = t.list_chunk(state,4)[0]
    return state











