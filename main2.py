import figury

print("program rozpoczol dzialanie")
while True:
    inp = input()
    if inp == "stop":
        print("program zakonczyl dzialanie")
        break
    elif inp == "a":
        a = float(input("a - "))
        print(f"v_kwadrat = {figury.v_kwadrat(a)}")
    elif inp == "b":
        a = float(input("a - "))
        b = float(input("b - "))
        print(f"v_prostokat = {figury.v_prostokat(a,b)}")
    elif inp == "c":
        a = float(input("a - "))
        h = float(input("h - "))
        print(f"v_rownoleglobok = {figury.v_rownoleglobok(a,h)}")
    elif inp =="d":
        a = float(input("a - "))
        b = float(input("b - "))
        h = float(input("h - "))
        print(f"v_trapez = {figury.v_trapez(a,b,h)}")
    elif inp == "e":
        a = float(input("a - "))
        h = float(input("h - "))
        print(f"v_trojkat = {figury.v_trojkat(a,h)}")
    elif inp == "f":
        a = float(input("a - "))
        print(f"v_trojrb = {figury.v_trojrb(a)}")
    elif inp == "g":
        r = float(input("r - "))
        print(f"v_kolo = {figury.v_kolo(r)}")
    elif inp == "h":
        e = float(input("e - "))
        f = float(input("f - "))
        print(f"v_romb = {figury.v_romb(e,f)}")