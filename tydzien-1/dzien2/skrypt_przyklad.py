def cezar_koduj(tekst,przesuniecie):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            baza = ord('A') if znak.isupper() else ord('a')
            nowy_kod = (ord(znak) - baza + przesuniecie) % 26 + baza
            wynik += chr(nowy_kod)
        else:
            wynik += znak
    return wynik

def cezar_deszyfruj(tekst,przesuniecie):
    return cezar_koduj(tekst,-przesuniecie)

print(cezar_koduj("Hello World!",3))
print(cezar_deszyfruj("Khoor Zroug!",3))