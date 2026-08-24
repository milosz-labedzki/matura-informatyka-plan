def sito(n):
    liczba = 2
    sito = [True] * (n+1)
    sito[0] = False
    sito[1] = False
    pierwiastek = n**0.5
    while(liczba<=pierwiastek):
        if(sito[liczba]==True):
            for wielokrotnosc in range(liczba*2, n+1, liczba):
                sito[wielokrotnosc] = False
        liczba += 1
    return sito


def pobierz_pierwsze(sito):
    lista = []
    for indeks, wartosc in enumerate(sito):
        if wartosc == True:
            lista.append(indeks)
    return lista

n = int(input("podaj liczbe do sprawdzenia: "))
wynik = sito(n)
lista = pobierz_pierwsze(wynik)
for x in lista:
    print(x, end=" ")
print(f"Znaleziono {len(lista)} liczb pierwszych")