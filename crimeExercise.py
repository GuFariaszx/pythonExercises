q1 = input("Telefonou para a vítima? ")
q2 = input("Esteve no local do crime? ")
q3 = input("Mora perto da vítima? ")
q4 = input("Devia para a vítima? ")
q5 = input("Ja trabalhou com a vítima? ")

result = 0
sim = ["Sim", "sim", "s", "S", "SIM", "SIm", "SiM", "yes", "YES", "y", "Y"]

if q1 in sim:
    result += 1
if q2 in sim:
    result += 1
if q3 in sim:
    result += 1
if q4 in sim:
    result += 1
if q5 in sim:
    result +=1

if result == 5:
    print(f"Você respondeu {result} vezes positivamente, então você é o assassino!")
elif 3 >= result <= 4:
    print(f"Você respondeu {result} vezes positivamente, então você é o Cúmplice!")
elif result == 2:
    print(f"Você respondeu {result} vezes positivamente, então você é o Suspeito!")
else:
    print(f"Você respondeu {result} vezes positivamente, então você é o Inocente!")


