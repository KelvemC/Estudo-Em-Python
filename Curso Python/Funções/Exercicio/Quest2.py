"""
02 - Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros).
"""


def potenciacao(base, expoente):
    return base**expoente


base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))
print(potenciacao(base=base, expoente=expoente))