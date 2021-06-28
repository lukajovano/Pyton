
import math
def primes_below(n):
    t=2
    l=[]
    while (t<n):
        m=0
        for i in l:
            if t%i==0:
                m=m+1
                break
            if (i>math.sqrt(t)):
                break

        if m==0:
            l.append(t)
        
        t=t+1
    return l