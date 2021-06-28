  
def to_hex(n):
    t1=n%16
    t2=n//16
    if (t1>9):
        s2=chr(t1+87)
    else:
        s2=str(t1)
    s1=""
    if(n>16):
        if (t2>9):
            s1=chr(t2+87)
        else:
            s1=str(t2)
    s=s1+s2
    return s

def hex_color (red, green, blue):
    r=""
    b=""
    g=""
    if (red<=16):
        r="0"
    if (green<=16):
        g="0"
    if (blue<=16):
        b="0"
    r=r+to_hex(red)
    g=g+to_hex(green)
    b=b+to_hex(blue)
    k="#"+r+g+b
    return k