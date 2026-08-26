def rozklad(n):
    lista = []
    d = 2
    while(n != 1):
        if(n % d == 0):
            lista.append(d)
            n = n // d
        else:
            d += 1
    return lista
print(rozklad(15))