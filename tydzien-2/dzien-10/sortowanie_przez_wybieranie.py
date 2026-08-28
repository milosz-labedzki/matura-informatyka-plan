def sortowanie_przez_wybieranie(tablica):
    n = len(tablica)
    for i in range (0,n-1):
        najmniejszy = i
        for j in range (i+1, n):
            if tablica[j] < tablica[najmniejszy]:
                najmniejszy = j
        temp = tablica[i]
        tablica[i] = tablica[najmniejszy]
        tablica[najmniejszy] = temp      
    return tablica

print(sortowanie_przez_wybieranie([5,3,8,1]))