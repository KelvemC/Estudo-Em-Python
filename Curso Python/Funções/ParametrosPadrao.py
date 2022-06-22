#Parâmetro Padrão
from curses.ascii import NUL

#para valores nulos, em python é 'None'
def imprimir_nome(nome=None, sobrenome=None, idade=None):
    print("nome:",nome)
    print("sobrenome:",sobrenome)
    print("idade:", idade)

imprimir_nome()
imprimir_nome(sobrenome="Fernandes", idade=20, nome="Kelvem")
