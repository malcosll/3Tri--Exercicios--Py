import math

def calcular_area(raio):
    return math.pi * (raio ** 2)

raio = float(input("Digite o raio do círculo: "))
area = calcular_area(raio)
print(f"A área do círculo é: {area:.2f}")