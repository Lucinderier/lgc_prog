#Faça um programa que imprima: cOs números de 1 a 100.
#qA
for num in range (101):
    print (num)
#irá printar uma lista de 1 a 100 no terminal, um abaixo do outro

#qB Os números pares de 50 a 100.

for num in range (50, 101, 2):
    print (num)

#qC Os números em contagem regressiva 10, 9, 8, 7,..., 1, 0 e Fogo!

for num in range(10, -1, -1):
    print(num)

#qD
valor = int(input("Digite um valor inteiro: "))
tipo = input("Digite 'par' para números pares ou 'impar' para números ímpares: ")

if tipo == "par":
    print(f"Números pares de 1 a {valor}:")
    for i in range(1, valor + 1):
        if i % 2 == 0:
            print(i, end=" ")
elif tipo == "impar":
    print(f"Números ímpares de 1 a {valor}:")
    for i in range(1, valor + 1):
        if i % 2 != 0:
            print(i, end=" ")
else:
    print("Opção inválida. Por favor, escolha 'par' ou 'impar'.")
