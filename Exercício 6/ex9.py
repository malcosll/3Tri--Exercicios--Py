def rotacionar_90(matriz):
    return [list(reversed(coluna)) for coluna in zip(*matriz)]