nomeAluno = str(input("Digite o nome do Aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceita nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"O aluno {nomeAluno} teve a média de {media}, portanto foi Aprovado!")
else:
    print(f"O aluno {nomeAluno} teve a média de {media}, portanto foi Reprovado!")
