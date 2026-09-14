lista1 = []
lista2 = []
magazyn = {}
cena_calkowita = 0

with open("magazyn.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(";")
        lista1.append(line)
    for slowo in lista1:
        nazwa = slowo[0]
        ilosc = int(slowo[1])
        cena = float(slowo[2])
        magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc
        cena_calkowita += ilosc*cena
    
with open("zamowienia.txt","r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        lista2.append(line)
unikalne = set(lista2)
w_magazynie = set(magazyn)
nieobecne = unikalne - w_magazynie

posortowane = sorted(magazyn.items(), key = lambda x:x[1], reverse=True)




for krotka in posortowane:
    print(f"{krotka[0]}: {krotka[1]}")
print(cena_calkowita)