import math
def is_prime(n):
    t=2
    l=[]
    while (t<=math.sqrt(n)):
        if n%t==0:
            return False
            break
        t=t+1
        if (t>=math.sqrt(n))and(n%t!=0):
            return True