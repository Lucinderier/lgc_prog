# Leitura dos dados do funcionário
matricula = input("Digite a matrícula do funcionário: ")

horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor que o funcionário recebe por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição da matrícula e do salário
print("Matrícula do funcionário:", matricula)
print("Salário do funcionário:", salario)
