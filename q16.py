# Dicionário para armazenar os contatos (nome: telefone)
agenda = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def buscar_contato():
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        print(f"O número de telefone de {nome} é: {agenda[nome]}")
    else:
        print(f"O contato {nome} não está na agenda.")

# Função principal para interagir com a agenda de contatos
def agenda_de_contatos():
    while True:
        print("\nAgenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            buscar_contato()
        elif escolha == '3':
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar a interação com a agenda de contatos
agenda_de_contatos()
