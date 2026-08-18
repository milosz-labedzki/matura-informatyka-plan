with open("dane.txt", "r", encoding="UTF-8") as f:
    suma_wiek = 0
    liczba = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        dane = line.split(";")
        imie=dane[0]
        wiek = int(dane[1])
        miasto = dane[2]
        suma_wiek += wiek
        liczba += 1
    print(f"Średni wiek: {suma_wiek/liczba:.2f}")