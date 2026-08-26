literka = 'b'
przesuniecie = 30
kod = ord(literka)- ord('a')
zmieniona_literka=(kod+przesuniecie) % 26
wynik = chr(zmieniona_literka + ord('a')) 
print(wynik)