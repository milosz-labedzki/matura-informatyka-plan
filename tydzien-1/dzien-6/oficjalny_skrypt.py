import sys
liczba_binarna = input("Podaj liczbę binarną do konwersji: ")
for i in liczba_binarna:
    if((i!="0" ) and (i !="1")):
        print("liczba nie jest binarna")
        sys.exit()
print(f"Liczba binarna {liczba_binarna} to w systemie dzisiętnym: {int(liczba_binarna,2)}")
liczba_heksadecymalna = hex(int(liczba_binarna,2))[2:].upper()
print(f"liczba w systemie heksadecymalnym to {liczba_heksadecymalna}")