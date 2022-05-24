"""
Sets são tipos de coleção: não ordenada, imutável e que não permite valores duplicados
"""

#Os sets também conhecidos como conjuntos
#nos sets você apenas vai utilizar os itens que você quer denifir no seu set
#não podemos fazer referência através do index ou chaves
#conjunto = {"item1","item2","item3", "item3", "item1"} se eu duplicar itens ele desconsidera(ignora eles)
"""
conjunto = {"item1",3, True, 4.7, "Cabrobó"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

conjunto = set((3,7,9,5))
print(conjunto)
print(type(conjunto))

conjunto = {3,7,9,5}

conjunto[0] = 4
print(conjunto)

#para acessar os itens do conjunto, é só fazer um loop através desse set
conj = {"item1", "item2","item3"}

for item in conj:
    print(item)
"""

conjunto = {"item",6,8,9,1}
print("item" in conjunto)

#as formas de acessar os itens de um conjunto é com o loop e o operador de associação 'in'

