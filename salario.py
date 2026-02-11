s = float(input("Informe seu salário mensal para reajuste: "))

reaj20 = s + s * 0.2
reaj15 = s + s * 0.15
reaj10 = s + s * 0.1
reaj5 = s + s * 0.05

if s >= 1500:
    perc5 = "5%"
    v = reaj5 - s
    print(f"Seu salário de R${s} recebeu {perc5} aplicado de aumento, sendo assim, aumentou {v} que totaliza R${reaj5}")
elif s >= 700 and s < 1500:
    perc10 = "10%"
    v = reaj10 - s
    print(f"Seu salário de R${s} recebeu {perc10} aplicado de aumento, sendo assim, aumentou {v} que totaliza R${reaj10}")
elif s > 280 and s < 700:
    perc15 = "15%"
    v = reaj15 - s
    print(f"Seu salário de R${s} recebeu {perc15} aplicado de aumento, sendo assim, aumentou {v} que totaliza R${reaj15}")
else:
    perc20 = "20%"
    v = reaj20 - s
    print(f"Seu salário de R${s} recebeu {perc20} aplicado de aumento, sendo assim, aumentou {v} que totaliza R${reaj20}")
