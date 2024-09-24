vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

produto = 1

for numero in vetor:
    produto *= numero

print(f"O produto de todos os elementos do vetor é: {produto}")