zliczenia = {}
slowo = "kotek"
for znak in slowo:
    if znak in zliczenia:
        zliczenia[znak] += 1
    else:
        zliczenia[znak] = 1

print(zliczenia)


   
