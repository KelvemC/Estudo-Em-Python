"""
Continue é usado em estruturas de repetições.
Pass é usado em estruturas condicionais.
"""

for x in range(10):
    if x ==3: continue #É um comando que para o laço atual e prossiga para o próximo laço de repetição onde x é = 4.
    #ignora o laço em que x = 3.
    print(x)

#pass é utilizado quando nós queremos aplicar ele dentro de condicionais vazias.

if x == 5:
    pass #ignore, porém muito cuidado ao usar pass

print("Olá mundo")