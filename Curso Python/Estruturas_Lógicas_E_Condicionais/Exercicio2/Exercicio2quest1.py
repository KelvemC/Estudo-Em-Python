"""
01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR
"""
idade = int(input("Insira sua idade: "))
if(idade < 16):
    print("MENOR")
elif(idade <=18):
    print("EMANCIPADO")
else:
    print("MAIOR")

