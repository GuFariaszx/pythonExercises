s = int(input("Digite seu salário: "))

while s < 5000:
    s += 100
    print(s)
    if s == 5000:
        print(f"Seu salário chegou a {s}")