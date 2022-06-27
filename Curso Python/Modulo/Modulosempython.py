#Módulo em python é os nomes para os arquivos em python

#Como interagir arquivos em python

#import random #Importando o módulo todo, não recomendável
#from random import random, choice
#print(random()) #Vai gerar resultado entre 0 e 1 mas ela não vai chegar nem 0 nem em 1.

#lista = ["pedra","papel","tesoura"]#Função que escolhe um valor aleatório  de uma lista.
#print(choice(lista))

#posso cria uma tupla para guardar na memória os dados que são importados
"""
from random import(
    random,
    choice,
    uniform
)
"""

#import random as rd #chamar funções de um módulo através de um apelido
from random import(
    random as rd,
    choice as ch,
    uniform as um
)
print(rd())




