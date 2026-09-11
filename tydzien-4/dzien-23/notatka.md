wygląd drzewa:

50 → 30 (lewe) 
50 → 70 (prawe) 
30 → 20 (lewe) 
30 → 40 (prawe)
70 → 60 (lewe)
70 → 90 (prawe)

        50
       /  \
      30    70
     / \    / \
    20 40  60  90


Jak liczyć krawędzie: po prostu policz ile linii łączy wierzchołki na rysunku. Tu: 50-30, 50-70, 30-20, 30-40, 70-60, 70-90 = 6 krawędzi.


Jak liczyć stopień wierzchołka: ile linii z niego wychodzi (licz też linię do rodzica, nie tylko do dzieci!). Np. 30 ma linię do 50 (rodzic) + do 20 + do 40 = stopień 3 (dodaj wszystkie stopnie razem, to musi wyjść 2 razy tyle co liczba krawędzi (bo każda krawędź liczy się dla dwóch końców). Tu: 2+3+3+1+1+1+1=12, a krawędzi jest 6, i 6×2=12 — zgadza się.)

Jak liczyć wysokość (długość) drzewa: licz kroki (krawędzie) od góry (korzeń) do najniżej położonego wierzchołka. Tu od 50 do 20 to 2 kroki — wysokość = 2.

Jak robić sortowanie (orders) — najprostszy sposób:

Podziel drzewo na 3 części: korzeń, cała lewa gałąź (30 z dziećmi 20,40), cała prawa gałąź (70 z dziećmi 60,90). Potem tylko układasz te 3 części w innej kolejności, zależnie co robisz:

pre-order (korzeń najpierw): korzeń → lewa gałąź → prawa gałąź → 50, 30, 20, 40, 70, 60, 90
in-order (korzeń w środku): lewa gałąź → korzeń → prawa gałąź → 20, 30, 40, 50, 60, 70, 90
post-order (korzeń na końcu): lewa gałąź → prawa gałąź → korzeń → 20, 40, 30, 60, 90, 70, 50

*nie wolno wstawić elementu z prawej gałęzi, dopóki cała lewa gałąź się nie skończy — nawet jeśli lewa gałąź ma swoje własne dzieci.*