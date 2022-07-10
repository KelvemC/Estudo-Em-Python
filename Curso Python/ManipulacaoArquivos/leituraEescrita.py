"""
arquivo = open('./Curso Python/ManipulacaoArquivos/receitas/brigadeiro.txt')
#print(arquivo.read()) #ler tudo de uma vez
print(arquivo.readline())#ler uma linha
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
Forma manual
"""
"""
with open('./Curso Python/ManipulacaoArquivos/receitas/brigadeiro.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)
print(arquivo.closed)
Forma pythoniana
"""
#existe um parâmetro implícito não obrigatório que podemos passar para que possamos realizar a escrita
#nele temos r para leitura e w para escrita

#quando abrimos o arquivo dessa forma sem passar nada, ele já executa como leitura
#o 'r' serve para leitura
#o 'w' vai sobrescrever tudo
#o 'a' vai anexar, colocando o texto no final do arquivo
texto = """
olá ola Ola
compras:
    pão
    leite
    suco
    frutas
"""
with open('./Curso Python/ManipulacaoArquivos/receitas/brigadeiro.txt', 'a') as arquivo:
    arquivo.write(f'\n{texto}')
  
