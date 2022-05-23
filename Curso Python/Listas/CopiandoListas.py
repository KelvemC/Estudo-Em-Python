lista = ["a", "b", "c"]
lista2 = lista.copy()

"""
lista2 = lista
lista2 = [1,4,6]
lista = lista + lista2
print(lista)

lista.extend(lista2)
print(lista)

for x in lista2:
    lista.append(x)
print(lista)
"""

#como copiar uma lista para outra lista
print(lista2)
#qualquer alteração que eu fizer em uma lista que copiei vai repecurtir na outra
#mas quando usamos a função copy isso não acontece
lista2.append("d")
print(lista)
print(lista2)