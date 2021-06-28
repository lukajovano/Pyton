
import math

def solve_quadratic(a,b,c):
    l=b*b-4*a*c
    if (l>0):
        l=b*b-4*a*c
        l1=math.sqrt(l)
        l1=math.floor(l1)
        l2=2*a
        n1=(-b+l1)//l2
        n2=(-b-l1)//l2
        n=(n1, n2)
        return n

    elif (l==0):
        return -b//(2*a)
    
    else:
        return None