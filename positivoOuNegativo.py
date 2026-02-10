n1 = float(input("Digite um número a sua escolha: "))
resultado = ("Positivo" * (n1 > 0)) + ("Negativo" * (n1 < 0)) + ("Zero" * (n1 == 0))

print(f"{n1} é um número: {resultado}")


