alunos = ["João", "Maria", "Pedro", "Ana"]
print("Versão 1: ", alunos)


alunos.append("Carlos")
alunos.append("Beatriz")
print("Versão 2: ", alunos)

alunos.sort()
print("Versão 3: ", alunos)

print("Insira um aluno a ser removido: ")
removido = input()

if(removido in alunos):
    alunos.remove(removido)
else:
    print("Aluno não encontrado")

if("Ana" in alunos):
    print("Posição: ", alunos.index("Ana"))
else:
    print("Ana não esta na lista")

if not alunos:
    print("Nenhum aluno restante")
else:
    print("Alunos restantes: ", alunos)