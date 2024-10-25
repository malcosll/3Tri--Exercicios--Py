def multiplicacao_matrizes(matriz_a, matriz_b):
    if len(matriz_a[0]) != len(matriz_b):
        return "Multiplicação impossível"
    return [[sum(a*b for a, b in zip(linha_a, coluna_b)) for coluna_b in zip(*matriz_b)] for linha_a in matriz_a]