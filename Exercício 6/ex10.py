def determinante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif len(matriz) == 3:
        return (matriz[0][0] * matriz[1][1] * matriz[2][2]
                + matriz[0][1] * matriz[1][2] * matriz[2][0]
                + matriz[0][2] * matriz[1][0] * matriz[2][1]
                - matriz[0][2] * matriz[1][1] * matriz[2][0]
                - matriz[0][0] * matriz[1][2] * matriz[2][1]
                - matriz[0][1] * matriz[1][0] * matriz[2][2])
    else:
        return "Apenas matrizes 2x2 ou 3x3 são suportadas."def determinante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif len(matriz) == 3:
        return (matriz[0][0] * matriz[1][1] * matriz[2][2]
                + matriz[0][1] * matriz[1][2] * matriz[2][0]
                + matriz[0][2] * matriz[1][0] * matriz[2][1]
                - matriz[0][2] * matriz[1][1] * matriz[2][0]
                - matriz[0][0] * matriz[1][2] * matriz[2][1]
                - matriz[0][1] * matriz[1][0] * matriz[2][2])
    else:
        return "Apenas matrizes 2x2 ou 3x3 são suportadas."