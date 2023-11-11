# Leitura do valor inteiro
tempo_em_segundos = int(input("Digite o tempo de duração em segundos: "))

# Cálculo das horas, minutos e segundos
horas = tempo_em_segundos // 3600
minutos = (tempo_em_segundos % 3600) // 60
segundos = tempo_em_segundos % 60

# Exibição do resultado no formato horas:minutos:segundos
print(f"O tempo de duração é: {horas:02d}:{minutos:02d}:{segundos:02d}")
