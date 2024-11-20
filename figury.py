import math
PI = math.pi

def v_kwadrat(a):
    return a*a

def v_prostokat(a,b):
    return a*b

def v_rownoleglobok(a,h):
    return a*h

def v_trapez(a,b,h):
    return ((a+b)*h)/2

def v_trojkat(a,h):
    return (a*h)/2

def v_trojrb(a):
    return (a**2*(math.sqrt(3)))/4

def v_kolo(r):
    return PI*(r**2)

def v_romb(e,f):
    return (e*f)/2