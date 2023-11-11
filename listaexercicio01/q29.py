import math

# Leitura do raio fornecido pelo usuário
raio = float(input("Digite o valor do raio da esfera: "))

# Atribuição do valor de PI
PI = 3.14159

# Cálculo do volume da esfera
volume = (4/3) * PI * raio ** 3

# Exibição do resultado
print(f"O volume da esfera com raio {raio} é: {volume:.2f}")
