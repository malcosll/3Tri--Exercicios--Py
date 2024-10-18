def contar_vogais(s):
    vogais = 'aeiouAEIOU'
    return sum(1 for letra in s if letra in vogais)