vetor = [0] * 5

for i in range(5):
    vetor[i] = float(input(f"Digite o elemento {i + 1}: "))

maior = vetor[0]

for i in range(1, 5):
    if vetor[i] > maior:
        maior = vetor[i]

print(f"O maior valor do vetor é: {maior}")