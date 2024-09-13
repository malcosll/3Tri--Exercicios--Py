minutos = int(input("Digite a quantidade de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{minutos} minutos correspondem a {horas} horas e {minutos_restantes} minutos.")