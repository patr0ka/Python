def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

print("Insira a quantia de numeros de fibonacci: ")
n = int(input())
fibonacci(n)