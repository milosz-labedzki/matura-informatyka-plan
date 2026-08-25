def NWD(a,b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a
def NWW(a,b,naj_wspolny_dziel):
    wartosc = (a * b) // naj_wspolny_dziel
    return wartosc
a = NWD(60,24)
print(f"NWD to: {a}")
n = NWW(60,24,a)
print(f"NWW to: {n}")

def rozklad(a):
    lista = []
    d = 2
    while(a != 1):
        if(a % d == 0):
            lista.append(d)
            a = a // d
        else:
            d += 1
    return lista

print(f"rozklad na czynniki pierwsze to: {rozklad(60)}")
            