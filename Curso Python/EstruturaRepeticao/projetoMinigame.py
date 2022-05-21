"""
do while

Código para adivinhar número
"""

palpite = 5
numero  = 9

while bool(palpite) is True:
    print("Qual é o número correto?")
    palpite = int(input())
    if(palpite == numero):
        print("Parabéns você acertou!")
        break
    else:
        print("Você errou")
else:
    print("Erro na aplicação!")




#bool() função que revela se algo é verdadeiro ou falso de maneira mais rápida
