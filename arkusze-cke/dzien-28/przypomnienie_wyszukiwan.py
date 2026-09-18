def wyszukaj_binarnie(tablica,x):
    p = 0
    k =  len(tablica)-1
    srodek = int((p+k)/2)
    while(tablica[srodek] != x):
        if(tablica[srodek]< x):
            p = srodek + 1
        if(tablica[srodek]> x):
            k = srodek - 1
        srodek = int((p+k)/2)
        if(p>k):
            return -1
    return srodek
print (wyszukaj_binarnie(tablica = [4,7,9,12,16,20,25,31,40],x=9))