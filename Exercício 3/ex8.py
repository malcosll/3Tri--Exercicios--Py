vetor = [0] * 5

for i in range(5):
    vetor[i] = input(f"Digite o elemento {i + 1}: ")

print("Os elementos na ordem inversa são:")
for i in range(4, -1, -1):
    print(vetor[i])