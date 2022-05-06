"""
02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras:
"""

idade = int(input("Insira a idade do nadador: "))
if(idade >=5 and idade <=7):
    print("Infantil A")
elif(idade >=8 and idade <=10):
    print("Infantil B")
elif(idade >=11 and idade <=13):
    print("Juvenil A") 
elif(idade >=14 and idade <=17):
    print("Juvenil B")
else:
    print("Fora da categoria")#Coloquei isso porque a questão não informa qual categoria um nadador com idade menor que 5 é ou maior que 17.