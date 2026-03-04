n1 = float(input("Digite um número a sua escolha: "))
resultado = ("Par" * (n1 % 2 == 0)) + ("Ímpar" * (n1 % 2 != 0))

print(f"{n1} é um número: {resultado}")
