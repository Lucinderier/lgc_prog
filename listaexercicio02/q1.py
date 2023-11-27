print("insira tres numeros")
num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
num3 = float(input("digite o terceiro numero: "))
if num1 >= num2 and num1>= num3:
    maior = num1
elif num2 >= num1 and num2>= num3:
    maior = num2
else:
    maior = num3

if num1<= num2 and num1<= num3:
    menor = num1
elif num2<= num1 and num2<= num3:
    menor = num2
else:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")