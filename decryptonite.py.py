import math

import random

def gcd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return(a)

n=int(input("enter public key:"))
temp_n=n
while (True):
    g=random.randint(1,n-1)
    if gcd(n,g)==1 and math.log(g)!=0:
        print("log(g)=",math.log(g))
        r=(math.log(n+1))//math.log(g)
        if(r%2==0): 
            r_ev_plus=(pow(g,r/2))+1
            while(r!=0):
                r=r_ev_plus%temp_n
                r_ev_plus=temp_n
                if r!=0:
                    temp_n=r
            q=n//temp_n
            p=n//q
            print(p,"\n",q)
            break
            
        else:
            continue
    else:
        continue
 





















