# Expressão 1
expressao1 = 3 < 2 ** 3 and 3 == 3
print("Resultado da Expressão 1:", expressao1)
# A ordem de execução é:
# 1. Avaliação de 2 ** 3 (2 elevado a 3) resulta em 8.
# 2. Avaliação de 3 < 8, que é verdadeiro.
# 3. Avaliação de 3 == 3, que também é verdadeiro.
# 4. Finalmente, avaliação da expressão True and True, resultando em True.

# Expressão 2
expressao2 = 0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2)
print("Resultado da Expressão 2:", expressao2)
# A ordem de execução é:
# 1. Avaliação de 0 != 4, que é verdadeiro.
# 2. Avaliação de (3/3 == 1), que é verdadeiro.
# 3. Avaliação de (5 + 1) / 3 == 2, que é falso.
# 4. Avaliação da expressão True or False, resultando em True.
