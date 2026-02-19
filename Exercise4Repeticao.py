soma = 0
repetir = 5

x = len(range(repetir))

for i in range(5):
    num = float(input(f"Digite o {i + 1} número: "))
    soma += num


media = ( soma / x )

print(f"Valor da Soma é: {soma}")
print(f"Valor da Média é: {media}")