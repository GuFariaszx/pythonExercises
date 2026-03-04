inicio = int(input("Digite o primeiro Número: "))

fim = int(input("Digite o segund número: "))

if inicio <= fim:
    passo = 1
else:
    passo = -1

print(f"Números entre o intervalo entre {inicio} e {fim}: ")

for i in range(inicio, fim + passo, passo):
    print(i, end = " ")

