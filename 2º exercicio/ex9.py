nota = float(input("Digite a nota (entre 0 e 10): "))

if nota >= 7:
    print("Aluno aprovado.")
elif 5 <= nota < 7:
    print("Aluno em recuperação.")
elif 0 <= nota < 5:
    print("Aluno reprovado.")
else:
    print("Nota inválida. A nota deve estar entre 0 e 10.")