vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

soma = sum(vetor)

media = soma / len(vetor)

print(f"A média dos elementos do vetor é: {media}")