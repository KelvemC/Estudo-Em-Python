#Argumento Arbitrário *args, usado quando não sabemos o n° de argumentos que uma função vai receber
#Essa função recebe argumentos que serão atribuídos em uma tupla.
def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem = None, *args):
    print('-'*20)
    print("Título:", nomeImovel)
    print("N° Quartos:", n_quartos)
    if vagasGaragem != None:
        print("Vagas na Garagem:", vagasGaragem)
#Exemplos de argumentos <= n° de parâmetros da minha função
imprimir_imovel("Casa 4 quartos - CABROBÓ(PE)", 4)

imprimir_imovel("Casa 6 quartos - SALGUEIRO(PE)", 6, 4)
#utilizando o argumento arbitrário args conseguimos passar mais argumentos
imprimir_imovel("Casa 6 quartos - SALGUEIRO(PE)", 6, 4, "Desconto")

"""
def imprimir_nomes(*nomes):
    print(nomes)

lista = ["Kelvem", "Marco", "Ericklis", "Willyam", "Neto", "Calleb"]
imprimir_nomes(lista)
"""