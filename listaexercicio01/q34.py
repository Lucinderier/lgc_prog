# Leitura dos dados fornecidos pelo usuário
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Cálculo do total em segundos
total_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos

# Exibição do resultado
print(f"O total em segundos é: {total_segundos} segundos.")
