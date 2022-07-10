import os

"""
Verificando a existência de arquivos e diretórios
"""
#Exemplo de caminho
print(os.path.exists('pastaNova/texto.py')) #Função que vai verificar se um arquivo ou diretório existe
#Exemplo de arquivo
print(os.path.exists('teste.txt'))
#Exemplo de diretório
print(os.path.exists('pastaNova'))

#Criando arquivos: para criar arquivos vamos usar os.mknod
#os.mknod('HelloWorld.py')

#criando arquivo em um diretório
#os.mknod('pastaNova/HelloWorld.py')

#criando um diretório: para cirar diretório usamos os.mkdir
#os.mkdir('codigosEmPython')

#Criando um diretório usando um caminho
#os.mkdir('codigosEmPython/codigos')

#Forma errada de usar caminhos relativos
#os.mknod('codigosEmPython/criacaoArquivo.txt')
#os.mknod('codigosEmPython/codigos/codigo.txt')

#podemos criar arquivos usando o caminho absoluto
#os.mknod('/home/kelvem/Documentos/DankiCode/Curso Python/ManipulacaoArquivos/creation.txt')

#usando caminho relativo, o './' serve para indicar a pasta atual que estamos
#os.mknod('./ManipulacaoArquivos/pastaNova/momonga.txt')

#criando diretório usando o caminho absoluto
#os.mkdir('/home/kelvem/Documentos/DankiCode/Curso Python/ManipulacaoArquivos/pastaNova/img')


#usando o relativo
#os.mkdir('./Curso Python/ManipulacaoArquivos/pastaNova/page')

#Apagando arquivos

#os.remove('teste.txt')
#print(os.path.exists('teste.txt'))
#os.remove('olamundo.py')
#os.remove('creation.txt')

#Apagando diretórios

#os.remove('codigosEmPython') #vai gerar um erro, porque precisamos usar uma função específica para deletar diretórios
#os.remove('./pastaNova/texto.py')
#os.rmdir('pastaNova') 
"""
Na função rmdir não conseguimos deletar diretório que contem arquivos,
caso tenha precisa deletar os arquivos.

Mas existe uma função para deletarmos diretórios com arquivos
"""

#renomear arquivos 

"""
os.mknod('olamundo.py')
os.makedirs('pastanova')
os.mknod('./pastanova/teste.txt')
"""

#A função rename como não passamos nenhum caminho seja relativo ou absoluto
#Essa função vai modificar apenas arquivos ou diretórios dentro do meu diretório atual

#os.rename('olamundo.py','olamundo.txt')
#os.rename('olamundo.txt', 'desenho.psd')

#Mudando nome do diretório
#os.rename('pastanova', 'pasta')

#OBS: precisa colocar o caminho novamente caso queira que a modificação ocorra somente naquele local
os.rename('./pasta/teste.txt', './pasta/compras.txt')