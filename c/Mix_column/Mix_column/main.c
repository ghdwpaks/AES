//xtime is a macro that finds the product of{ 02 }and the argument to xtime modulo{ 1b }
#define xtime(x)   ((x<<1) ^ (((x>>7) & 1) * 0x1b))
// MixColumns function mixes the columns of the state matrix
// The method used may look complicated, but it is easy if you know the underlying theory.
// Refer the documents specified above.
void MixColumns()
{
    int i;
    unsigned char Tmp, Tm, t;
    int state[4][4] = { {212,191,93,48},{224,180,82,174},{184,65,17,241},{30,39,153,229 } };
    //int state2[4][4] = { d4,bf,5d,30,e0,b4  ,52,ae,b8  ,41,11,f1,1e,27,98,e5};
    //int state[4][4];

    for (i = 0; i < 4; i++)
    {
        t = state[0][i];

        Tmp = state[0][i] ^ state[1][i] ^ state[2][i] ^ state[3][i];



        Tm = state[0][i] ^ state[1][i];
        Tm = xtime(Tm); 
        state[0][i] = state[0][i] ^ (Tm ^ Tmp);



        Tm = state[1][i] ^ state[2][i];
        Tm = xtime(Tm); 
        state[1][i] ^= Tm ^ Tmp;



        Tm = state[2][i] ^ state[3][i]; 
        Tm = xtime(Tm); 
        state[2][i] ^= Tm ^ Tmp;



        Tm = state[3][i] ^ t; 
        Tm = xtime(Tm); 
        state[3][i] ^= Tm ^ Tmp;
    }
}


//                                                       This source code Copyright belongs to Crocus
//                                                        If you want to see more? click here >>
