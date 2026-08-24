def czy_pierwsza(n):
    start = 2
    liczba = 2
    pierwiastek = n ** 0.5
    if(n<=1):
         print("liczba jest nie poprawna")
         return False
    while(liczba>=start and liczba <= pierwiastek):
        if(n%liczba==0):
                return False
        liczba+=1
    return True
print(czy_pierwsza(2137))