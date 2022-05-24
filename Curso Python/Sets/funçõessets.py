conjunto1 = {1,5,3,2}
conjunto2 = {3,6,2}
"""
Utilizando funções principais dos sets: 

#para usar essa função é preciso criar outra variável, já a função update não precisa
conjunto3 = conjunto1.union(conjunto2) #função que serve para unir conjuntos
print(conjunto3)

conjunto1.intersection_update(conjunto2)
print(conjunto1)
"""
#imprimindo elementos que não se repetem
#sobrescreveu os valores anteriores, lembrando que não houve modificação
conjunto1.symmetric_difference_update(conjunto2)

print(conjunto1)