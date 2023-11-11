# Leitura do valor do salário do usuário
salario = float(input("Digite o valor do salário: "))

# Expressão para determinar se a pessoa deve pagar imposto
deve_pagar_imposto = salario > 1200.00

# Exibição do resultado
print("Paga imposto?", deve_pagar_imposto)
