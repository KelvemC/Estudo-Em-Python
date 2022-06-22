"""
01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;
"""

def maior(x,y):
    if(x>y):
        return x
    else:
        return y


def media_aritmetica(x,y):
    return (x+y)/2


numero1 = float(input("Insira o valor de X: "))
numero2 = float(input("Insira o valor de Y: "))

print(f"Maior número entre X e Y: {maior(numero1, numero2)}")
print(f"Média aritmética entre X e Y: {media_aritmetica(numero1, numero2)}")

