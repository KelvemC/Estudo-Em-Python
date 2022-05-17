import random
"""
Olá, fiz esse pequeno projeto
Usei o modulo random para gerar número aleatórios, o usuário
vai tentar adivinhar o número que foi gerado e terá condições para
tentar ajudar ele a saber se o número que foi digitado é igual
ao que foi gerado ou não. 

Também terá um contador de tentativas. 
"""
numero =  random.randint(0,10)
laco = True
contador_tentativas = 0
print("\n")
print("adivinhe o número".title())
while(laco == True):
    palpite = int(input("Insira o seu palpite: "))
    print("\n")
    if(palpite == numero):
        print("Acertou!!")
        contador_tentativas +=1
        laco = False
    elif(palpite > numero):
        print(f"{palpite} é maior que o número")
        contador_tentativas += 1
    else:
        print(f"{palpite} é menor que o número")
        contador_tentativas += 1

print("\n")
print("Fim das tentativas")
print("\n")
if(contador_tentativas == 1):
    print("Você conseguiu acertar de primeira ;)")
elif(contador_tentativas > 1):
    print(f"A quantidade de tentativas que você teve até acertar foi {contador_tentativas} vezes.")