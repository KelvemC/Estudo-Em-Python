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

print("Aŕea de um Retângulo")
base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
areaRetangulo = base*altura
print(f"A área do retângulo é = {areaRetangulo} cm²")

#02
print("Área de um Quadrado")
lado = int(input("Insira um lado: "))
areaQuadrado = lado**2
print(f"A área do quadrado é = {areaQuadrado} cm²")

#03
produto = float(input("Informe o produto que deseja avaliar valor: "))
desconto = float(input("Informe o desconto do produto que deseja avaliar: "))
resultado = produto - (produto * desconto /100)

print(f"O produto que você quer avaliar custa {produto:.2f} reais, o valor do mesmo com o desconto de {desconto}% é = {resultado:.2f}.")

#04
print("Aréa de um Círculo")
raio = float(input("Informe o raio: "))
pi = 3.14
areaCirculo = pi * raio**2
print(f"A área de um círculo é = {areaCirculo} cm²")


#05
print("Conversão de Reais para Dolar")
cotacao = 4.96
reais = float(input("Insira um valor em dolar: "))
converter = reais / cotacao
print(f"O valor {reais} em reais convertido para dolar é = {converter:.2f}")



#06
print("Conversão de Dolar para Reais")
reais = 4.96
dolar = float(input("Insira um valor em dolar: "))
converter = dolar * reais
print(f"O valor {dolar} em dolar convertido para reais é = {converter:.2f}")
