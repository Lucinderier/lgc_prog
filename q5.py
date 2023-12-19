def adicao():
    print("Tabuada de Adição:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} + {j} = {i + j}")
        print("------------")

def subtracao():
    print("Tabuada de Subtração:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} - {j} = {i - j}")
        print("------------")

def multiplicacao():
    print("Tabuada de Multiplicação:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
        print("------------")

def divisao():
    print("Tabuada de Divisão:")
    for i in range(1, 11):
        for j in range(1, 11):
            if j != 0:
                print(f"{i} / {j} = {i / j}")
            else:
                print(f"{i} / {j} = Indefinido")
        print("------------")

while True:
    print("\nEscolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = input("Digite o número correspondente à operação desejada: ")

    if escolha == '1':
        adicao()
    elif escolha == '2':
        subtracao()
    elif escolha == '3':
        multiplicacao()
    elif escolha == '4':
        divisao()
    elif escolha == '5':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
