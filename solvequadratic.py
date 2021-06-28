import math

a = int(input('a= ')) 
b = int(input('b= ')) 
c = int(input('c= ')) 

d=b**2-4*a*c 

if d < 0: 
    print('The equation has no real solution') 
elif d == 0: 
    x=(-b)/(2*a) 
    print('This equation has one solution ',x) 
else: 
    x1 = (-b+math.sqrt(d))/(2*a) 
    x2 = (-b-math.sqrt(d))/(2*a) 
    print('This equation has two solutions: ',x1, 'or',x2) 