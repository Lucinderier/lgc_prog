# Leitura do valor de ponto flutuante
valor_monetario = float(input("Digite o valor monetário (com duas casas decimais): "))

# Multiplica o valor por 100 para trabalhar com números inteiros
valor_centavos = int(valor_monetario * 100)

# Inicializa o contador de notas e moedas
notas_100 = notas_50 = notas_20 = notas_10 = notas_5 = notas_2 = 0
moedas_1 = moedas_050 = moedas_025 = moedas_010 = moedas_005 = moedas_001 = 0

# Cálculo das notas
while valor_centavos != 0:
    if valor_centavos >= 10000:
        valor_centavos -= 10000
        notas_100 += 1
    elif valor_centavos >= 5000:
        valor_centavos -= 5000
        notas_50 += 1
    elif valor_centavos >= 2000:
        valor_centavos -= 2000
        notas_20 += 1
    elif valor_centavos >= 1000:
        valor_centavos -= 1000
        notas_10 += 1
    elif valor_centavos >= 500:
        valor_centavos -= 500
        notas_5 += 1
    elif valor_centavos >= 200:
        valor_centavos -= 200
        notas_2 += 1
    elif valor_centavos >= 100:
        valor_centavos -= 100
        moedas_1 += 1
    elif valor_centavos >= 50:
        valor_centavos -= 50
        moedas_050 += 1
    elif valor_centavos >= 25:
        valor_centavos -= 25
        moedas_025 += 1
    elif valor_centavos >= 10:
        valor_centavos -= 10
        moedas_010 += 1
    elif valor_centavos >= 5:
        valor_centavos -= 5
        moedas_005 += 1
    elif valor_centavos >= 1:
        valor_centavos -= 1
        moedas_001 += 1

# Exibição do resultado
print(f"Notas de R$ 100: {notas_100}")
print(f"Notas de R$ 50: {notas_50}")
print(f"Notas de R$ 20: {notas_20}")
print(f"Notas de R$ 10: {notas_10}")
print(f"Notas de R$ 5: {notas_5}")
print(f"Notas de R$ 2: {notas_2}")
print(f"Moedas de R$ 1: {moedas_1}")
print(f"Moedas de R$ 0.50: {moedas_050}")
print(f"Moedas de R$ 0.25: {moedas_025}")
print(f"Moedas de R$ 0.10: {moedas_010}")
print(f"Moedas de R$ 0.05: {moedas_005}")
print(f"Moedas de R$ 0.01: {moedas_001}")
