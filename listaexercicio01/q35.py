import math

# Leitura do valor do lado do quadrado
lado_quadrado = float(input("Digite o valor do lado do quadrado: "))

# Cálculo do perímetro, área e diagonal
perimetro = 4 * lado_quadrado
area = lado_quadrado ** 2
diagonal = lado_quadrado * math.sqrt(2)

# Exibição dos resultados
print(f"Perímetro do quadrado: {perimetro:.2f}")
print(f"Área do quadrado: {area:.2f}")
print(f"Diagonal do quadrado: {diagonal:.2f}")

