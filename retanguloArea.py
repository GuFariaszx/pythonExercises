ladoRetangulo = float(input('Digite o lado do Retângulo:'))
baseRetangulo = float(input('Digite a base do Retângulo:'))

somaDosLados = ladoRetangulo + ladoRetangulo + baseRetangulo + baseRetangulo
resultPerimetro = somaDosLados
resultArea = ladoRetangulo * baseRetangulo

print(f'O perímetro de seu Retângulo é {resultPerimetro:.2f}')
print(f'A Área de seu Retângulo é {resultArea:.2f}')