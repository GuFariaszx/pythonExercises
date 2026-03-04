from datetime import datetime

ano_atual = datetime.now().year

s = float(input("Digite o salário inicial: "))
ano = 1985
print(f"Ano de {ano}, salário não multiplicado, totalizando R${s:.2f}")


ano = 1986
perc = 0.015 
s += s * perc
print(f"Ano de {ano}, salário multiplicou {perc}, totalizando R${s:.2f}")


while ano < ano_atual:
    ano += 1
    perc *= 2
    s += s * perc
    print(f"Ano de {ano}, salário multiplicou {perc}, totalizando R${s:.2f}")
    
    