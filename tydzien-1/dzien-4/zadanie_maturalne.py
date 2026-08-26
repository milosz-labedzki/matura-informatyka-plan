slowo = input("Podaj słowo do przetworzenia: ")
slownik = {}
for znak in slowo:
    if znak == " ":
        continue
    slownik[znak] = slownik.get(znak,0) + 1
for litera in slownik:
    print(litera,slownik[litera])
