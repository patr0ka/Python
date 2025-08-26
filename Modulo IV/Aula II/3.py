nomes = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
for membro in nomes:
    vogais=0
    for letra in membro:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vogais+=1
    print("Vogais em ", membro, ": ", vogais)
