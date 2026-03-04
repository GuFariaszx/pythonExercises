name = input("Informe seu nome para registro: ")
v = float(input("Digite o valor da sua compra: "))

if v < 0:
    print(f"{name} o valor informado não pode ser registrado, por favor tente novamente!")
elif v <= 100:
    print(f"{name} sua compra teve o valor de R${v}")
elif 100 < v < 200:
    d1 = v - (v*0.1)
    print(f"{name} sua compra teve o valor de R${v}, com 10% de desconto ficou: R${d1}")
elif 200 < v < 500:
    d2 = v - (v*0.2)
    print(f"{name} sua compra teve o valor de R${v}, com 20% de desconto ficou: R${d2}")
elif v >= 500:
    d3 = v - (v*0.3)
    print(f"{name} sua compra teve o valor de R${v}, com 30% de desconto ficou: R${d3}")
