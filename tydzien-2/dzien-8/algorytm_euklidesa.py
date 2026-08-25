def NWD(a,b):
    while(b != 0):
        r = a%b
        a=b
        b=r
    return a
def NWW(a,b,naj_wspolny_dzielnik):
    wartosc = (a*b)/naj_wspolny_dzielnik
    return wartosc
a = NWD(48,18)
print(NWW(48,18,a))