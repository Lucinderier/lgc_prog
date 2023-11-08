# Exibe o menu de opções
print("Menu de Opções:")
print("1. Opção 1 (Número 15)")
print("2. Opção 2 (Número 35)")
print("3. Opção 3 (Número 50)")

opcao = input("Escolha uma opção (1/2/3): ")


opcao = int(opcao)


if opcao == 1:
    print("Você escolheu a Opção 1 (Número 15).")
elif opcao == 2:
    print("Você escolheu a Opção 2 (Número 35).")
elif opcao == 3:
    print("Você escolheu a Opção 3 (Número 50).")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1/2/3).")
