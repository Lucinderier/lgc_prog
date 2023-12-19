#recursiva :)
def contagem_regressiva_recursiva(n):
    if n <= 0:
        print("Fogo!")
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

n = int(input("Digite um número inteiro para a contagem regressiva (Recursiva): "))
contagem_regressiva_recursiva(n)

#iterativa
def contagem_regressiva_iterativa(n):
    while n > 0:
        print(n)
        n -= 1
    print("Fogo!")

n = int(input("Digite um número inteiro para a contagem regressiva (Iterativa): "))
contagem_regressiva_iterativa(n)
