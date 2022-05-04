"""
Python - Comandos de Controle Condicional

if, else e elif -> (else if)


aluno = str(input("Informe o nome do aluno: "))
nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
media = (nota1+nota2)/2

print(f"A média do aluno {aluno} é = {media}")
if(media >=7):
    print(f"O aluno {aluno} foi aprovado!")
else:
    print(f"O aluno {aluno} foi reprovado!")

print("Fim do programa!")
"""

print("programa para calcular o imc".title())
peso = float(input("Insira seu peso em KG: "))
altura = float(input("Insira a sua altura: "))
IMC = peso/altura**2

print(f"seu imc é = {IMC:.1f}")
if(IMC < 18.5):
    print("Abaixo do peso!")
elif(IMC <=24.9):
    print("Normal!")
elif(IMC <=29.9):
    print("Sobrepeso!")
elif(IMC <40):
    print("Obesidade")
else:
    print("Obesidade grave!")
