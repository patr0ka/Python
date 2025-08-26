def jokenpo(escolha1,escolha2):
    if escolha1 == escolha2:
        print("Empate!")
    elif escolha1 == "Pedra" and escolha2 == "Tesoura" \
    or escolha1 == "Papel" and escolha2 == "Pedra" \
    or escolha1 == "Tesoura" and escolha2 == "Papel":
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")
    

print("Jogador 1 insira sua escolha: (Pedra, Papel ou Tesoura)")
escolha1 = input().capitalize()
print("Jogador 2 insira sua escolha: (Pedra, Papel ou Tesoura)")
escolha2 = input().capitalize()

jokenpo(escolha1, escolha2)

