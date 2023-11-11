# Leitura dos dados do vendedor
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
vendas_efetuadas = float(input("Digite o valor total de vendas efetuadas no mês: "))

# Cálculo da comissão (15% das vendas)
comissao = vendas_efetuadas * 0.15

# Cálculo do total a receber no final do mês (soma do salário fixo e da comissão)
total_a_receber = salario_fixo + comissao

# Exibição do resultado
print(f"O vendedor {nome_vendedor} receberá no final do mês: R$ {total_a_receber:.2f}")
