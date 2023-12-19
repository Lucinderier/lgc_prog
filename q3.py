numeros = []
total = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break #break para sair
    numeros.append(numero)
    total += numero

quantidade = len(numeros)
if quantidade > 0:
    media = total / quantidade
    print(f"\nQuantidade de números digitados: {quantidade}")
    print(f"Soma dos números: {total}")
    print(f"Média dos números: {media}")
else:
    print("Nenhum número foi digitado.")
