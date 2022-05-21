maior = 0
menor = 0
print("Programa que ler 5 valores e encontra o maior e menor entre eles.")
for i in range(5):
    numero = int(input("Insira um número: "))
    if(i == 0): maior = numero; menor = numero
    elif (numero > maior): maior = numero
    elif (numero < menor): menor = numero
print(f"O maior número é {maior} e o menor número é {menor}")