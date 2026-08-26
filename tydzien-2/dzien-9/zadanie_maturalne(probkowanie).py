def wyszukiwanie_binarne(lista,szukana):
    left = 0
    right = len(lista)-1
    probki = 0
    while(left<=right):
        mid = (left+right) // 2
        probki += 1
        if(lista[mid] == szukana):
            return probki
        else:
            if(szukana > lista[mid]):
                left = mid + 1
            else:
                right = mid - 1
    return -1
print(f"Liczba próbek {wyszukiwanie_binarne([1,2,3,4,5,6,7,8,9,10,11,12,13],6)}")
