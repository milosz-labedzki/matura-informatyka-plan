zliczenia = {}
with open("liczby.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = int(line)
        reszta = line % 3
        zliczenia[reszta] = zliczenia.get(reszta, 0) + 1
print(f"Liczba zliczen dla kazdej liczby to {zliczenia}")