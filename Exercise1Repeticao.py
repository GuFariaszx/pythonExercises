n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

for i in range(n1 + 1, n2) or range(n2 + 1, n1):
    print(f"Os números inteiros entre {n1} e {n2}, são: {i}")