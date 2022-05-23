#index      0         1       2
lista = ["carro", "barco", "avião"]
print(lista)

#adicionando elementos em uma lista
#lista.append(["moto", "bicicleta", "navio" ])#append, adiciona um novo elemento no final da lista
#lista.insert(1,"bicicleta") #adiciona elemento em qualquer posição da lista.
lista.extend(["bicicleta", "navio"]) #adiciona na lista vários elementos separadamente, sem tar dentro de uma lista
for x in range(len(lista)): print(f"[{x}] =", lista[x])


"""
texto = "meunome@gmail.com"
lista2 = list(texto)
print(lista2)

texto = texto.split('@')
print(texto)
"""
