"""
Função FromKeys: retorna valores como chaves, e podem ser utilizados 
principalmente para criar dicionários
a partir de listas ou tuplas"""

tupla = ("item1", "item2", "item3")
tupla2 = (0,1,2)
dicio = dict.fromkeys(tupla)
#podemos passar outra argumento, que seria os valores, só que ele iria atribuir a todas as chaves.
#dicio = dict.fromkeys(tupla,tupla2)
print(dicio)

#aninhamento de dicionários
dic = {
    "dicio1": dicio,
    "nome": 'kelvem',
    "idade": 20
}

print(dic)

