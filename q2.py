#a
def multiplicacao_soma(num1, num2):
    resultado = 0
    for _ in range(abs(num2)):
        resultado += abs(num1)
    
    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        return -resultado
    else:
        return resultado


resultado = multiplicacao_soma(4, 5)
print("Resultado da multiplicação:", resultado)

#b
def divisao_e_resto(dividendo, divisor):
    quociente = 0
    resto = abs(dividendo)
    
    while resto >= abs(divisor):
        resto -= abs(divisor)
        quociente += 1
    
    if (dividendo < 0 and divisor > 0) or (dividendo > 0 and divisor < 0):
        quociente = -quociente
        resto = -resto
    
    return quociente, resto

quociente, resto = divisao_e_resto(20, 4)
print("Quociente da divisão:", quociente)
print("Resto da divisão:", resto)