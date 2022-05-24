"""
Não conseguimos modificar itens de um conjunto que já foi definido
Nenhuma referência

Mas temos funções que adiciona, remove e copía

Adicionando elementos

set1 = {"item1","item2","item3"}
print(set1)

set1.add("item4")
print(set1)

set1.add(8)
set1.add(True)
print(set1)

set1 = {4,5,7,8,9,1}
set2 = {"item3", "item5", "item1"}
set1.update([1,4,7,8,9,3,"item6"]) #Outra forma de adicionar elementos
print(set1)
"""

#forma de remover elementos

set1 = {1,3,4,5,"item5", 7,8,9,"item6"}
print(set1)

set1.pop()#como set não é ordenado, a cada impressão a ordem dele muda, então na lógica em relação aos sets o pop remove itens aleatórios. 
print(set1)

#função remove
set1.remove("item5") #se tentar remover um item que não existe vai dar erro.
print(set1)

#função discard

set1.discard("item80") #se tentar remover um item que não existe não vai dar erro. 
print(set1)

"""
del set1
print(set1)
"""
set1.clear()
print(set1)
