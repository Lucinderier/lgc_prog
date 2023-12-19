#qA
def area_quadrado (lado):
    area = lado ** 2
    return area
print(area_quadrado(4))  
print(area_quadrado(9))

#qB
def area_triangulo (base, altura):
    area = (base * altura) / 2
    return area
print(area_triangulo(6, 9))
print(area_triangulo(5,8))

#qC
def area_quadrado(lado, exibir=False):
    area = lado ** 2
    if exibir:
        print(f"A área do quadrado com lado {lado} é: {area}")
    return area

def area_triangulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"A área do triângulo com base {base} e altura {altura} é: {area}")
    return area

area_quadrado(4, True) 
area_quadrado(9, True)  

area_triangulo(6, 9) 
area_triangulo(5, 8, True)  