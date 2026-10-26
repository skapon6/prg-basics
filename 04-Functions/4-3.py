from math import sqrt

def triangle_area(a,b,c):
    s = 0.5*(a+b+c)
    area =  sqrt(s*(s-a)*(s-b)*(s-c))
    return area
    

print(triangle_area(7,24,25))