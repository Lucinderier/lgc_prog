valor = int(input("Digite o valor a ser decomposto em notas: "))
print(f"Valor lido: {valor}")

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = [0, 0, 0, 0, 0, 0, 0]  #quantidades de notas

for i, nota in enumerate(notas):
    while valor >= nota:
        valor -= nota
        quantidades[i] += 1

for i, nota in enumerate(notas):
    if quantidades[i] > 0:
        print(f"{quantidades[i]} nota(s) de {nota}")

