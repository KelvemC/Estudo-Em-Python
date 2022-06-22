"""
03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10.
"""

#Fiz uma calculadora simples mas que consegue realizar as função da calculadora do windows 10
from math import sqrt
def menu():
    return """
    -------------------------
    ==========MENU===========
    ( 1 ) = %
    ( 2 ) = 1/x
    ( 3 ) = x²
    ( 4 ) = ²√X
    ( 5 ) = ÷
    ( 6 ) = x
    ( 7 ) = -
    ( 8 ) = +
    ( 9 ) = +/-
    =========================
    """
    

def escolha():
    esc = (input("Escolha uma das opções do Menu: "))
    return esc


def modulo():
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return (numero1/100) * numero2
    

def inverso_numero():
    numero = float(input("Insira um valor: "))
    return 1/numero
   

def potenciacao():
    numero = float(input("Insira um valor: "))
    return numero**2
   

def raiz_Ao_quadrado():
    numero1 = float(input("Insira o valor 1: "))
    return sqrt(numero1)


def divisao():
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1/numero2


def multi():
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1*numero2


def subtracao():
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1-numero2


def soma():
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1+numero2


def nevativar():
    numero = float(input("Insira um valor: "))
    return -numero


def calculadora():
    print(menu())
    esc = escolha()
    
    if esc == '1': return modulo()
    elif esc == '2': return inverso_numero()
    elif esc == '3': return potenciacao()
    elif esc == '4': return raiz_Ao_quadrado()
    elif esc == '5': return divisao()
    elif esc == '6': return multi()
    elif esc == '7': return subtracao()
    elif esc == '8': return soma()
    elif esc == '9': return nevativar()
    else: print(f"\033[31mDigita uma opção correta\033[m"); return calculadora()
    

print(calculadora())