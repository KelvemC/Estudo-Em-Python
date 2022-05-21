palpite = 5
numero  = 9

while True:
    print("Qual é o número correto?")
    palpite = int(input())
    if(palpite == numero):
        print("Parabéns você acertou!")
        break
    else:
        print("Você errou")
else:
    print("Erro na aplicação")
    print(bool(palpite))