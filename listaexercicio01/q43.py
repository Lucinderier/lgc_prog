# Leitura das notas do aluno em cada matéria
materia1 = float(input("Digite a nota da primeira matéria: "))
materia2 = float(input("Digite a nota da segunda matéria: "))
materia3 = float(input("Digite a nota da terceira matéria: "))

# Leitura do número total de faltas do aluno
total_faltas = int(input("Digite o número total de faltas: "))

# Cálculo da média do aluno
media_aluno = (materia1 + materia2 + materia3) / 3

# Cálculo da frequência do aluno (considerando 30 aulas no total)
frequencia = ((30 - total_faltas) / 30) * 100

# Verificação se o aluno foi aprovado
aprovado = media_aluno > 7 and frequencia >= 75

# Exibição do resultado
print("Aluno aprovado?", aprovado)
