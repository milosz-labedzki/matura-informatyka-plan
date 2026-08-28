def sortowanie_przez_wybieranie():
    T = [9,4,6,2,7]
    n = len(T)
    liczba_porownan = 0
    for i in range (0,n-1):
        najmniejszy = i
        for j in range (i+1, n):
            if T[j] < T[najmniejszy]:
                najmniejszy = j
            liczba_porownan += 1
        temp = T[i]
        T[i] = T[najmniejszy]
        T[najmniejszy] = temp
        print(f"Stan tablicy po kazdej rundzie: {T}")
    print(f"Liczba porownan to: {liczba_porownan}")

def sortowanie_malejaco():
    T = [9,4,6,2,7]
    n = len(T)
    for i in range (0,n-1):
        najwiekszy = i
        for j in range (i+1, n):
            if T[j] > T[najwiekszy]:
                najwiekszy= j
        temp = T[i]
        T[i] = T[najwiekszy]
        T[najwiekszy] = temp 
             
    print(f"Lista malejąca to {T}")
print(sortowanie_przez_wybieranie())
print(sortowanie_malejaco())

