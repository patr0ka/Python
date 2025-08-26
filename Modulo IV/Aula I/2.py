a = int(input())
b = int(input())
c = int(input())

def imprimeCrescente(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(a, b, c)


imprimeCrescente(a, b, c)