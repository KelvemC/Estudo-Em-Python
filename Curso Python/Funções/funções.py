"""
#Paradigma imperativo:
paradigmas são conhecidos como tipos de programação
exemplo: programação Orientada a Objeto e a imperativa.
O paradigma imperativo além dele ser antigo é natural e se baseia no modo de funcionamento do computador.

Características: variáveis, atribuições e principalmente sequêncial.
Linguagens que usa esse paradigma: C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2.
"""

nome = "Gabriel"

"""
Função, nada mais é do que um bloco de código, uma declaração e outros comandos que pode ser
nomeada e chamada de dentro de um programa.

Função é uma sequência de comandos que recebe um nome e que pode ser chamada em qualquer parte do programa.
"""

#palavra chave para definir função é 'def'


def minha_funcao(): 
    #bloco interno: conhecido com corpo da função.
    nome = "Ana" #variável local
    tupla = 2,5,6,9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Olá ana")


#executando função
minha_funcao()
#bloco externo
print(nome)