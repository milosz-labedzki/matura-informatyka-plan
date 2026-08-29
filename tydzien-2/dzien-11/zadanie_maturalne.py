lista = []
lista_palindromow = []
lista_anagram = []
def czy_palindrom():
    with open("slowa.txt","r",encoding="UTF-8") as f:
        for line in f:
            slowo = line.strip()
            lista.append(slowo)
            slowo_odwrot = slowo[::-1]
            if(slowo == slowo_odwrot):
                lista_palindromow.append(slowo)
    return lista_palindromow
print(f" palindromy to: {czy_palindrom()}")

def czy_anagramy():
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(sorted(lista[i])==sorted(lista[j])):
                lista_anagram.append((lista[i],lista[j]))
    return lista_anagram
print(f"lista anagramow to: {czy_anagramy()}")