#concatenação de tuplas
tupla = ("item1","item2","item3")
(x,*y) = tupla
print(x)
print(y)
"""
print(x)
print(y)
print(z)
tupla2 = ("a", "b")
tupla += tupla2 * 3
print(tupla)

for x in range(len(tupla)):
    print(f"({x}) =", tupla[x])
"""