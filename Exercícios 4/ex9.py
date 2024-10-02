numero = 29
primo = True
i = 2
while i * i <= numero:
    if numero % i == 0:
        primo = False
        break
    i += 1
print(f"{numero} é primo: {primo}")