"""
Como achar o fatorial de um número

Como eu fiz:

numero = int(input("Insira o número: "))
result = 1
if numero>=0: 
    for i in range(1 ,numero+1): result*=i
    print(f"O !{numero} = {result}")
else: print(f"Fatorial de número negativo não existe, você digitou {numero}")
"""
"""
Olá, tentei fazer de outra forma, que no caso foi exibir como é feito o calculo
"""
fatorial = 1
numero  = int(input("Insira um número: "))
if numero < 0: print("Não existe fatorial de número negativo!")
elif numero == 0: print(f"O fatorial de {numero} = 1")
else: 
    print(f"!{numero}", end=", ")
    for i in range(1, numero+1): fatorial *= i
    for x in range(numero, 0, -1): print(f"{x}", end=" * ") if x > 1 else print(f"{x}", end=" = ")
    print(fatorial)
