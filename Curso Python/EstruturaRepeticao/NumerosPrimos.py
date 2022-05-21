"""
Como descobrir número primo
"""

print(30 * "-")
numero = int(input("Insira o número: "))

if numero > 1:
    #Verificando resto das divisões
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Esse não é um número primo")
            break
    else:
        print("Esse número é primo")
else:
    print("Esse número não é primo: número menor ou igual a 1")
print(30 * "-")

