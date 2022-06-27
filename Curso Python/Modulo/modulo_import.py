#from random import * #forma de importar tudo

#modulo - arquivos com extensão .py - ou seja - arquivos python
#pacotes - diretórios contendo conjunto de módulos - pastas com vários arquivos python 

#como importar modulos de pacotes
#from pacote import principal, secundaria
#para chamar uma sub-pasta é assim:
from pacote.sub_diretorio import outro as modulo


print(modulo.cubica(5))