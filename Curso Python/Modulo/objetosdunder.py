"""
Objetos Dunder
Dunder - duplo Underscore - Duplo Underline
Conhecido como Atributos Mágicos - variáveis
Métodos Mágicos - funções

Os objetos dunder são utilizados para linguagem python usar internamente.

Objetos dunder principais

__init__ - Python 2.x precisava criar o arquivo init, ele é um arquivo .py vazio, do qual a linguagem das versões anteriores iria entender que aquilo é um pacote python

__name__ O dunder name vai receber o nome do arquivo, e se ele estiver sendo execultado diretamente, se ele for o modulo principal de execução, ele vai mostrar somente o print
__main__

__file__
__doc__ - Docstrings, usado para documentação dos nossos módulos

Uso de # é para exemplos
Uso de """""" fazem parte da documentação

Não é bom utilizar o __doc__ diretamente no módulo para definir documentação
"""



import random
import primo
print(primo.primo(5))
