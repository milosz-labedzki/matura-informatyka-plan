def wspolne_elementy(lista1,lista2):
    zbior1 = set(lista1)
    zbior2 = set(lista2)
    wynik = sorted(zbior1 & zbior2)
    return wynik
print(wspolne_elementy([1,2,3,4,5],[2,3,4,5,6,7]))