"""
Operadores Lógicos e o tipo boolean

Em ciência da computação, boolean, ou lógico,
é um tipo de dado primitivo que possui dois valores,
que podem ser considerados como (0 ou 1), falso ou verdadeiro.

É chamado boolean em homenagem a George boole
"""

# Tipo boolean : True e False

"""
Operadores lógicos

and (e)
or (ou)
not (negação)

"""
#Tabela verdade (and): para que o resultado seja verdadeiro ambos os lados(expressões) tem que ser verdadeiro.
print(True and True)
print(True and False)
#Tabela verdade (or): para que o resultado seja verdadeiro basta que um dos lados(expressões lógicas) sejam verdadeiro, se os dois for falso então a expressão vai ser falsa.
print(True or True)
print(True or False)

#Tabela verdade(not): ele nega uma expressão lógica, exemplo not True, ele está negando o True, e a negação de True é False, fazendo com que ele vire falso.
print(not True)