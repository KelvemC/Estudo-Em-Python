#Dicionários: coleção não ordenada, mutável e que não permite valores duplicados
#         key   :   value         o valor pode ser definido depois dos dois pontos
from curses import keyname


dicio = {"nome":"Kelvem","ano":2002,"valor_lógico":True}
print(dicio)

dicionario = {
    "nome":"Kelvem",
    "idade":20,
    "sexo":"M",
    "nacionalidade": "Brasileiro"
}

print(dicionario)
#os itens que não podem ser duplicados se encontram nas chaves(keys), caso coloque
#uma chave igual e um valor diferente, o valor antigo será reescrito.

#acessar os itens do dicionário:
#dicionario[chave]
print(dicionario['nome'])

#outra forma de acessar os itens e valores
print(dicionario.get('idade'))

print(dicionario.keys()) #função que retorna todas as chaves que meu dicionário possui

print(len(dicionario))

print(dicionario.values()) #função que retorna todos os valores que meu dicionário possui.

#verificando os valores de chave se existem.
if "idade45" in dicionario:
    print("A chave idade existe")

#dicionários são conhecidos como mapas.

print(dicionario.items()) #função que retorna cada item do dicionário como se fosse uma tupla dentro de uma lista.

#como modificar os valores do dicionário

print(dicio)

dicio['nome'] = 'Carlos'
print(dicio)

#outra forma de modificar um valor de alguma chave

#tem que passar como argumento dicionários.
dicio.update({"nome":"Ana"})
print(dicio)

#quando passamos uma chave e um valor que não existe dentro de um dicionário, essa nova chave
# e valor é inserido dentro do nosso dicionário
dicio['idade'] = 20
print(dicio)

#posso usar o update também
dicio.update({"estado":"PE"})
print(dicio)


#removendo itens de um dicionário:

dicio.popitem() #remove o item final do dicionário, apenas na versão 3.7 ou acima, na versão abaixo da 3.7, ela elimina um item aleatório.
print(dicio)

#removendo um item específico, o item é eliminado com base na chave
dicio.pop('valor_lógico')
print(dicio)

#podemos usar o del também:
del dicio['nome']

print(dicio)

# deletando dicionário
"""
del dicio
print(dicio)

Limpando dicionário sem destruir ele:
"""
dicio.clear()
print(dicio)

print("\n")
#loop em dicionário:
for x, y in dicionario.items():
    print(x, y)

dicio = dicionario.copy()
print(dicio)

dicio2 = dict(dicio)
dicio.update({'trabalha?': False})
print(dicio2)