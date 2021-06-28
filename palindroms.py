
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


i=10000
l=[]
while (i<100000):
    if (i//10000==i%10) and ((i//1000)%10==(i%100)//10) and is_prime(i):
        l.append(i)
    i=i+1

print(l)