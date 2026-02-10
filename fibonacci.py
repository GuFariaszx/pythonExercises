n = int(input("Digite quantos termos da sequência Fibonacci: "))

n1 = 0
n2 = 1

print(f"Sequência Fibonacci com {n} termos:")
for i in range(n):
    if n != None:
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2

