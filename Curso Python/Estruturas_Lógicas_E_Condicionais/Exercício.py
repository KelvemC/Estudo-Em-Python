"""
Observações: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa(??) reais qual
será o valor do mesmo com o desconto de (??)%.
04 - área de um círculo - pi = 3,14
05 - conversão de reais para dolar
06 - conversão de dolar para reais
"""

#01
from unittest import result


print("Aŕea de um retângulo")
base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
areaRetangulo = base*altura
print(f"A área do retângulo é = {areaRetangulo} cm²")

#02
print("Área de um quadrado")
lado = int(input("Insira um lado: "))
areaQuadrado = lado**2
print(f"A área do quadrado é = {areaQuadrado} cm²")

#03
produto = float(input("Informe o produto que deseja avaliar valor: "))
desconto = float(input("Informe o desconto do produto que deseja avaliar: "))
resultado = produto - (produto * desconto /100)

print(f"O produto que você quer avaliar custa {produto:.2f} reais, o valor do mesmo com o desconto de {desconto}% é = {resultado:.2f}.")