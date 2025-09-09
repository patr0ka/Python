import random
import string

def oitoletra():
    caracter = string.ascii_letters
    senha = ''.join(random.choice(caracter) for _ in range(8))
    print(senha)

def oitoletranum():
    caracter = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracter) for _ in range(8))
    print(senha)

def oitotudo():
    caracter = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracter) for _ in range(8))
    print(senha)

print("Escolha o tipo da senha: (1, 2, 3)")
print("Oito letras - 1")
print("Oito letras/numeros - 2")
print("Oito de tudo - 3")
x = int(input())
match x:
    case 1:
        oitoletra()
    case 2:
        oitoletranum()
    case 3:
        oitotudo()
    