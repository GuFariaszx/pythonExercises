total = 0
quantidade = 0

while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): "))

    if preco == 0:
        break

    while preco < 0:
        print("Valor Inválido")
        preco = float(input("Digite o preço do produto novamente: "))
        if preco == 0:
            break

    if preco == 0:
        break

    total += preco
    quantidade += 1

print("\nFECHAMENTO DO CAIXA")

if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print(f"Total da compra: R$ {total:.2f}")
print(f"Quantidade de itens: {quantidade}")
print(f"Média por produto: R$ {media:.2f}")

if quantidade > 0:
    forma = int(input("\nForma de pagamento (1 - Dinheiro / 2 - Cartão): "))

    if forma == 1:
        desconto = total * 0.05
        total_com_desconto = total - desconto
        print(f"Desconto de 5% aplicado: R$ {desconto:.2f}")
        print(f"Total com desconto: R$ {total_com_desconto:.2f}")
    elif forma == 2:
        print("Pagamento no cartão. Sem desconto.")
    else:
        print("Forma de pagamento inválida.")
else:
    print("Nenhum produto foi registrado.")



    