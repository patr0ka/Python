import random
import string

def geraSenha(tipo):
    if tipo == 1:
        caracteres = string.ascii_letters
    elif tipo == 2:
        caracteres = string.ascii_letters + string.digits
    elif tipo == 3:
        caracteres = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(8))

def sistemaCadastro():
    usuarios = {}
    while True:
        nome = input("Digite o nome de usuário (ou 'sair' para encerrar): ")

        if nome.lower() == "sair":
            print("Encerrando o programa")
            break

        if nome in usuarios:
            print("Este nome já existe")
            continue

        print("Escolha o tipo de senha:")
        print("1 - Apenas letras")
        print("2 - Letras e números")
        print("3 - Tudo")
        try:
            tipo = int(input("Digite sua opção: "))
        except ValueError:
            print("Entrada inválida, usando padrão (2 - letras e números).")
            tipo = 2

        senha = geraSenha(tipo)
        usuarios[nome] = senha
        print(f"Usuário '{nome}' cadastrado com a senha: {senha}")

    print("=== LISTA FINAL DE USUÁRIOS CADASTRADOS ===")
    for usuario, senha in usuarios.items():
        print(f"{usuario}: {senha}")

sistemaCadastro()
