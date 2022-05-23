#tuplas: pode ser interpreta como uma variável que consegue guardar na memória múltiplos itens
lista = ["item1", "item2", "item3"]
print(lista)
print(len(lista))
print(type(lista))

print(50 * '-')
tupla = ("item1","item2","item3", "item1")
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla.count("item1"))
#diferença: ambas são variáveis que consegue armazenar diversos itens em sua memória, ambas são ordenáveis.
#A tupla ela é imutável

#reescrevi a variável tupla, eu não adicionei elementos, não modifiquei elementos, não apaguei elementos
tupla = (1,2,3,4)
print(tupla)

#exemplo de quando usar as tuplas:
unidade_federativas = ("SP", "DF", "GO", "SS")
print(type(unidade_federativas))

#tuplas aceita vários tipos de elementos
tupla = (3,5.0, True, "Olá")
print(tupla)

tupla = ("item1")
print(type(tupla))
#foi a mesma coisa que criar uma string
#para resolver isso é só fazer isso:
tupla= ("item1",)
print(tupla)
print(type(tupla))

#O que faz a tupla ser uma tupla é a ',' não os parênteses

#transformando tupla em lista
lista = list(tupla)
lista.extend(["item2","item3","item4","item5"])
print(lista)
lista.pop()

tupla = tuple(lista)
print(tupla)

del tupla
print(tupla)