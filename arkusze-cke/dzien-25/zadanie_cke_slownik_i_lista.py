lista = []
lista2 = []
slownik = {}
with open("magazyn.txt","r",encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(";")
        lista.append(line)
    for slowo in lista:
        nazwa = slowo[0]
        liczba = int(slowo[1])
        cena = float(slowo[2])
        slownik[nazwa] = slownik.get(nazwa,0)+liczba

with open("zamowienia.txt","r",encoding="UTF-8") as f:
        for line in f:
            line = line.strip()
            lista2.append(line)
            unikalne = set(lista2)
w_magazynie = slownik.keys()
brakujace = unikalne - w_magazynie
posortowane = sorted(slownik.items(), key= lambda x:x[1], reverse=True)
print(brakujace)
print(posortowane)