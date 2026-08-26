def szyfr_cezara():
    tekst = "kod"
    przesuniecie = 3
    nowy_napis = ""
    for znak in tekst:
        szyfr = ord(znak) - ord('a')
        przesuniety_tekst = (szyfr+przesuniecie) % 26
        nowy_napis+=chr(przesuniety_tekst+ ord('a'))
    print(nowy_napis)
print(szyfr_cezara())