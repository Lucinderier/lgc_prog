
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# notas dentro do intervalo [0, 10]
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    # Cálculo da média 
    media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

    # Impressão da média
    print("Média Ponderada:", media_ponderada)
else:
    print("Por favor, digite notas dentro do intervalo de 0 a 10.")
    
