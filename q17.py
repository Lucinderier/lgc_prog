agenda = {}  # Aqui é onde o dicionário é inicializado para armazenar os contatos

# As funções adicionar_contato() e buscar_contato() operam diretamente sobre o dicionário 'agenda':
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda[nome] = telefone  # Adiciona o contato ao dicionário

def buscar_contato():
    nome = input("Digite o nome do contato: ")
    contato = agenda.get(nome)  # Busca o contato no dicionário
    if contato:
        print(f"O número de telefone de {nome} é: {contato}")
    else:
        print(f"O contato {nome} não está na agenda.")

# A função principal agenda_de_contatos() controla a interação com o dicionário 'agenda'
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

agenda_de_contatos()  # Inicia a interação com a agenda de contatos
