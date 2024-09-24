vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

contador_pares = 0

for numero in vetor:
    if numero % 2 == 0:
        contador_pares += 1

print(f"A quantidade de números pares no vetor é: {contador_pares}")