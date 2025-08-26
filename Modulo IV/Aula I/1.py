def isTriangulo(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        if a == b == c:
            return "Equilátero"
        elif a == b or a ==c or b ==c:
            return "Isóceles"
        else:
            return "Escaleno"
    else:
        return "Não forma um triangulo"
    

a = int(input())
b = int(input())
c = int(input())

print(isTriangulo(a, b, c))