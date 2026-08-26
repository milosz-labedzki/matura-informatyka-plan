def unikalne_oceny(klasa_a,klasa_b):
    zbior1 = set(klasa_a)
    zbior2 = set(klasa_b)
    wynik = sorted(zbior1 ^ zbior2)
    return wynik
print(unikalne_oceny([1,3,4,5,4,3,6,5,2],[5,6,6,4,3,2,2,5]))