#função que tenta modificar um valor imutável (emulação de passagem por valor)
def passagem_por_valor(x):
    print("Valor original dentro da função:", x)
    x += 5
    print("Valor após a modificação dentro da função:", x)

#ex de uso para passagem por valor (emulação)
valor = 10
print("Valor original antes da função:", valor)
passagem_por_valor(valor)
print("Valor original após a função:", valor)

#função que modifica uma lista (passagem por referência)
def passagem_por_referencia(lista):
    print("Lista original dentro da função:", lista)
    lista.append(4)
    print("Lista após a modificação dentro da função:", lista)

#exemplo de uso para passagem por referência
minha_lista = [1, 2, 3]
print("Lista original antes da função:", minha_lista)
passagem_por_referencia(minha_lista)
print("Lista original após a função:", minha_lista)
