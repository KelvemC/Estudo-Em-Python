"""
lista = ["chicago", "queens", "cabrobó", "pernambuco"]
print(lista)

lista2 = [2,4,50,7,8,10]
print(lista2)

lista3 = [2.50, 4.3, 5.50]
print(lista3)

lista4 = [True, False]
print(lista4)

lista5 = [True, "cabrobó", 2.5, False, 4]
print(lista5) 

print("\n")

#em python temos a ordem dos index, que no caso da lista5 é 0 a 4
#porém se pegarmos o index -1, estaremos girando como uma roda e indo para o elemento final
# resumindo um contagem da ordem oposta.


#Slicing é um recurso que vem da biblioteca numpy, muito utilazada com vetores:

print(lista5[::])
print(lista5[1:]) #retorna do index que destacamos até o fim da lista.
print(lista5[2:]) #retorna do segundo index até o último da lista.
print(lista5[:3]) # retorna do começo da lista até o index -1.
print(lista5[:4]) # retorna do começo da lista até o index -1.
print(lista5[1:4]) # retorna do index destacado até o index -1.

print("\n")

print(lista5[1:4:2])

#Slicing com String:

nome = "terra"
print(nome[2:4:])


lista2 = lista2 + lista3
print(lista2)
"""

lista1 = [2.0,3.5,4.7]
print(lista1)

lista2 = [1,5,9,11,15]
print(lista2)
#index     0         1        2
lista3 = ["Nome", "Nome2", "Nome"]
#comprimento/tamanho da lista
#tamanho da lista - função len 
print(len(lista1))
print(len(lista2))
print(len(lista3))

#Funções que só conseguem ser utilizadas com tipos de dados númericos
print(sum(lista1)) #somatório dos elementos da nossa lista

print(max(lista2)) # retorna o elemento de valor máximo da lista
print(max(lista1)) # retorna o elemento de valor máximo da lista(maior valor da lista)

print(min(lista1)) # retorna o elemento de valor mínimo da lista(menor valor da lista)

