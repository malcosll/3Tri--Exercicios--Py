vetor = [0] * 5

for i in range(5):
    vetor[i] = float(input(f"Digite o elemento {i + 1}: "))

maior = vetor[0]
menor = vetor[0]

for numero in vetor:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

diferenca = maior - menor

print(f"A diferença entre o maior e o menor valor é: {diferenca}")