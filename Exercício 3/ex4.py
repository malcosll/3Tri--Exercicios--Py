vetor = [0] * 5


for i in range(5):
    vetor[i] = float(input(f"Digite o elemento {i + 1}: "))

menor = vetor[0]

for i in range(1, 5):
    if vetor[i] < menor:
        menor = vetor[i]

print(f"O menor valor do vetor é: {menor}")