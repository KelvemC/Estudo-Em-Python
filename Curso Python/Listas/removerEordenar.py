"""
lista = ["carro", "barco", "avião"]
print(lista)
"""

#lista.pop() #função que remove o último elemento da lista
#lista.remove("barco")#função que remove elemento específico da lista
#na função pop pode ser passado como argumento o index que deseja remover
#lista.pop(0)
#função del: deletar lista e deletar item específico da lista
#del lista[0]
#del lista

"""
carrinho_de_compras = ["pão", "carne", "verduras", "alface"]
#arrinho_de_compras.clear()#função que apaga todos os elementos da lista, mas não apagar a existência da lista.

#odernando itens de uma lista:
carrinho_de_compras.sort() #ordena elementos de uma lista de forma alfabética
for x in range(len(carrinho_de_compras)): print(f"[{x}] =", carrinho_de_compras[x])
print(carrinho_de_compras)

#a função sort funciona com números
lista = [9,7,50,11,13,2,22,0,99]
lista.sort()
print(lista)

#como ordenar lista de números de forma decrescente
lista.sort(reverse=True)
print(lista)
"""

lista = ["Ana", "Pedro", "Marta", "Clarice", "beatriz"]
print(lista)
lista.sort(key = str.lower)#organiza os elementos da lista, tratando eles como se fosse todos minúsculos.
print(lista)
