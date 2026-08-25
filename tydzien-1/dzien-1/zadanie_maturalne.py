with open("produkty.txt","r", encoding="UTF-8") as f:
    najwyzsza_wartosc =0
    ilosc = 0
    cena_ogolna= 0
    ilosc_produktow_wiekszych=0
    produkt_najdrozszy=""
    for line in f:
        line = line.strip()
        if not line:
            continue
        dane = line.split(";")
        produkt = dane[0]
        cena = float(dane[1])
        ilosc = int(dane[2])
        wartosc = cena * ilosc
        cena_ogolna +=  wartosc
        if wartosc>najwyzsza_wartosc:
            najwyzsza_wartosc = wartosc
            produkt_najdrozszy = produkt
        if cena > 50:
            ilosc_produktow_wiekszych+=1
    print(f"Najwyższa łączna całość {najwyzsza_wartosc} jest to produkt: {produkt_najdrozszy}")
    print(f"Cena wszystkich łącznie to: {cena_ogolna}")
    print(f"Cena produktów wiekszych od 50: {ilosc_produktow_wiekszych}")
