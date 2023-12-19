def contem_item(lista, item):
    for elemento in lista:
        if elemento == item:
            return True
    return False

def merge_listas(lista1, lista2):
    lista_resultante = lista1[:]  #copia de lista um para a lista resultante
    
    for item in lista2:
        if not contem_item(lista_resultante, item):
            lista_resultante.append(item)
    
    return lista_resultante


lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]

lista_sem_repeticao = merge_listas(lista_a, lista_b)
print("Lista resultante sem elementos repetidos:", lista_sem_repeticao)

#a

def merge_listas(lista1, lista2):
    lista_resultante = lista1[:]  
    
    for item in lista2:
        encontrado = False
        for elemento in lista_resultante:
            if elemento == item:
                encontrado = True
                break
        
        if not encontrado:
            lista_resultante.append(item)
    
    return lista_resultante


#lista_a = [1, 2, 3, 4, 5]
#lista_b = [3, 4, 5, 6, 7]

lista_sem_repeticao = merge_listas(lista_a, lista_b)
print("Lista resultante sem elementos repetidos:", lista_sem_repeticao)
