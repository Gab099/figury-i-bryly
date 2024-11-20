import math
PI = math.pi

def v_porostobloscian(a,b,c):
    return a*b*c

def v_koli(r):
    return 4/3*PI* r**3

def v_szescian(a):
    return 6*a**2

def v_walec(r,H):
    return (2*PI* r**2) + (2*PI* r*H)

def v_stozek(r,l):
    return (PI*r**2) + (PI*r*l)

def v_graniastoslup(Pp,Pb):
    return (2*Pp) + Pb