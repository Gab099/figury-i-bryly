
import bryly


print("Program rozpoczol dzialanie ;)")
while True:
    inp = input()
    if inp == "stop":
        print("Progam zkonczyl dzilanie")
        break
    elif inp == "a":
        a = float(input("a - "))
        b = float(input("b - "))
        c = float(input("c - "))
        print(f"v_porostobloscian = {bryly.v_porostobloscian(a,b,c)}")
    elif inp == "b":
        r = float(input("r - "))
        print(f"{bryly.v_koli(r)}")
    elif inp == "c":
        a = float(input("a - "))
        print(f"v_szescian = {bryly.v_szescian(a)}")
    elif inp == "d":
        r = float(input("r - "))
        H = float(input("H - "))
        print(f"v_walec = {bryly.v_walec(r,H)}")
    elif inp == "e":
        r = float(input("r - "))
        l = float(input("l - "))
        print(f"v_stozek = {bryly.v_stozek(r,l)}")
    elif inp == "f":
        Pp = float(input("Pp - "))
        Pb = float(input("Pb - "))
        print(f"v_graniastoslup = {bryly.v_graniastoslup(Pp,Pb)}")
    else:
        print("Nie ma takiej komendy")

