srednia_ocen = []
imie =""
najwyzsza_srednia=0
najlepszy_uczen =""
with open("uczniowie.txt", "r", encoding="UTF-8") as f:
    for dane in f:
        dane = dane.strip()
        if dane=="":
                    continue
        dane = dane.split(",")

        srednia_liczbowa = float(dane[2])

        srednia_ocen.append(srednia_liczbowa)

        suma_srednich = sum(srednia_ocen) / len(srednia_ocen)

        srednia_zaokraglona = round(suma_srednich,2)

        if srednia_liczbowa > najwyzsza_srednia:
            najwyzsza_srednia = srednia_liczbowa
            najlepszy_uczen = dane[0]

    print(f"srednia ocen wszystkich to:{srednia_zaokraglona} a najlepszy uczen to: {najlepszy_uczen}")