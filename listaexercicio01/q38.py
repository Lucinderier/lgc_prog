# Leitura do valor inteiro correspondente à idade em dias
idade_em_dias = int(input("Digite a idade em dias: "))

# Cálculo dos anos, meses e dias
anos = idade_em_dias // 365
meses = (idade_em_dias % 365) // 30
dias = (idade_em_dias % 365) % 30

# Exibição dos resultados
print(f"A idade em anos, meses e dias é: {anos} anos, {meses} meses e {dias} dias.")
