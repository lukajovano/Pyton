
def big_fibonacci(n):
    i1=0
    i2=1
    i=i1+i2
    while len(str(i))<n:
        i1=i2
        i2=i
        i=i1+i2
    
    return i