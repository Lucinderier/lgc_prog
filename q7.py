def verifica_parenteses(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return "Erro" 
            pilha.pop() 
    
    if not pilha:
        return "OK"  
    else:
        return "Erro"  

#entrada do usuário
expressao = input("Digite a expressão com parênteses: ") #abre uma caixa para digitar a expressão

resultado = verifica_parenteses(expressao)
print(resultado)

