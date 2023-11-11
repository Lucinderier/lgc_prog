# Leitura do valor inteiro
valor = int(input("Digite um valor inteiro: "))

# Inicializa o contador de notas
notas_100 = notas_50 = notas_20 = notas_10 = notas_5 = notas_2 = notas_1 = 0

# Cálculo das notas
while valor != 0:
    if valor >= 100:
        valor -= 100
        notas_100 += 1
    elif valor >= 50:
        valor -= 50
        notas_50 += 1
    elif valor >= 20:
        valor -= 20
        notas_20 += 1
    elif valor >= 10:
        valor -= 10
        notas_10 += 1
    elif valor >= 5:
        valor -= 5
        notas_5 += 1
    elif valor >= 2:
        valor -= 2
        notas_2 += 1
    elif valor >= 1:
        valor -= 1
        notas_1 += 1

# Exibição do resultado
print(f"O valor lido foi: {valor}")
print("Notas:")
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 2: {notas_2}")
print(f"Notas de 1: {notas_1}")
