"""
Trocando variáveis
"""

# Trocando variáveis em python

x = input("Insira o valor de x: ") #a
y = input("Insira o valor de y: ") #b

# Criaremos uma variável temporária

temp = x #temp = a
x = y #x = y(b)
y = temp #y(b) = a

print(f"O valor de x depois da troca é {x}")
print(f"O valor de y depois da troca é {y}")