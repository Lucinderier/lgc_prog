def bubble_sort(lista):
    tamanho = len(lista)

    
    for i in range(tamanho - 1):
        for j in range(0, tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp

lista = [7, 4, 3, 12, 8]

#ordenando a lista usando o Bubble Sort
bubble_sort(lista)

print("Lista ordenada em ordem crescente:", lista)
