n = float(input("Digite um número para vizualizar sua tabuada até o 10: "))

for i in range(10):
    tab = n * i
    print(f"{n} * {i} = {tab}")