T = [-10, -8, 0, 1, 2, 5, -2, -4]

#minima temp
menor_temperatura = min(T)

#maior temp
maior_temperatura = max(T)

#calculando a temperatura média,  sum para somar
temperatura_media = sum(T) / len(T)

print(f"Menor temperatura: {menor_temperatura}°C")
print(f"Maior temperatura: {maior_temperatura}°C")
print(f"Temperatura média: {temperatura_media:.2f}°C")
