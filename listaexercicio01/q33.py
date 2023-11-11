# Leitura dos dados fornecidos pelo usuário
tempo_viagem_horas = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media_kmh = float(input("Digite a velocidade média durante a viagem (em km/h): "))

# Definição da eficiência do automóvel em km por litro
eficiencia_automovel = 12  # 12 km/L

# Cálculo da distância percorrida
distancia_percorrida = tempo_viagem_horas * velocidade_media_kmh

# Cálculo da quantidade de litros necessários
litros_necessarios = distancia_percorrida / eficiencia_automovel

# Exibição do resultado
print(f"Para a viagem de {distancia_percorrida:.2f} km, Joãozinho precisaria de {litros_necessarios:.2f} litros de combustível.")
