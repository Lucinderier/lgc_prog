# Leitura dos dados fornecidos pelo usuário
distancia_percorrida_km = float(input("Digite a distância total percorrida (em km): "))
combustivel_gasto_litros = float(input("Digite o total de combustível gasto (em litros): "))

# Cálculo do consumo médio
consumo_medio = distancia_percorrida_km / combustivel_gasto_litros

# Exibição do resultado
print(f"O consumo médio do automóvel é: {consumo_medio:.2f} km/l")
