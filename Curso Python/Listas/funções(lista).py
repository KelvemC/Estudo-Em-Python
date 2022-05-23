nome = "curso-python"
valor = range(10)

#transformando um string e um range em lista
"""
print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list(nome)
print(lista8)
"""
#checando elemento dentro da lista
lista7 = list(range(10))

elemento = int(input("Insira o elemento: "))
if elemento in lista7:
    print("Este elemento está dentro da lista")
