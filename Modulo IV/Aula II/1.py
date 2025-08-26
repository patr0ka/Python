estoque = ["Camisa", "Calça", "Blusa", "Jaqueta"]
print("Versão 1: ", estoque)

estoque.append("Sapato")
print("Versão 2: ", estoque)

estoque.insert(2, "Boné")
print("Versão 3: ", estoque)

if("Chapéu" in estoque):
    estoque.remove("Chapéu")
else:
    print("Chapéu não está no estoque")

estoque.sort

print("Versão final: ", estoque)

