#Argumento arbitrário **Kwargs - Keyword Arguments (Argumentos nomeados)
# Essa função recebe argumentos que serão atribuídos em um dicionário
#Kwargs diferente do args é utilizado quantos argumentos nomeados vamos passar como argumento na nossa função

def imprimir_nomes(**kwargs):
    print(f"{kwargs['nome']} {kwargs['sobrenome']}")

imprimir_nomes(nome="Ana", sobrenome = "Fernandes")

