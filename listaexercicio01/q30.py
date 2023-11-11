import math

# Leitura dos valores fornecidos pelo usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Cálculo da área do triângulo retângulo
area_triangulo = (a * c) / 2

# Cálculo da área do círculo
raio_circulo = c
area_circulo = math.pi * (raio_circulo ** 2)

# Cálculo da área do trapézio
area_trapezio = ((a + b) * c) / 2

# Cálculo da área do quadrado
area_quadrado = b ** 2

# Cálculo da área do retângulo
area_retangulo = a * b

# Exibição dos resultados
print(f"A área do triângulo retângulo é: {area_triangulo:.2f}")
print(f"A área do círculo é: {area_circulo:.2f}")
print(f"A área do trapézio é: {area_trapezio:.2f}")
print(f"A área do quadrado é: {area_quadrado:.2f}")
print(f"A área do retângulo é: {area_retangulo:.2f}")
