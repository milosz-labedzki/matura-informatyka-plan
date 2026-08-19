wyniki = []
wynik = 0
with open("dane.txt", "r") as f:
    for dane in f:
        dane = dane.strip()
        if dane=="":
            continue
        dane = dane.split(",")
        wzrost = int(dane[1])
        wyniki.append(wzrost)
        print(dane)
    for i in wyniki:
        wynik += i
    srednia = wynik / len(wyniki)
#print(wyniki)
print(srednia)