lista_de_tarefas = []

#adicionando
def adicionar_tarefa(tarefa):
    global lista_de_tarefas
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

#exibindo todas tarefas
def exibir_tarefas():
    global lista_de_tarefas
    if lista_de_tarefas:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(lista_de_tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Lista de tarefas vazia.")

adicionar_tarefa("Ler livro")
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer compras")

exibir_tarefas()
