print("ola")
print('ola')

w = "Curso de python3"
print(w)

"""comentário"""
#a razão disso acima não ser interpretado é porque é uma string e ela não está salva na memória.

a = """ola,
este é o curso de python
espero que goste"""

print(a)

#métodos das strings

b = " Olá mundo "
print(b.strip())
#o método strip serve para ignorar os espaços antes e depois da frase que digitei.

c = "Olá Mundo!"
print(c.lower())

#O método lower serve para deixar as letras em minúsculo.

d = "olá mundo!"
print(d.upper())

#o Método upper serve para deixar as letras em maiúsculo.

e = "Olá,"
f = "Mundo!"
g = e +" " + f
print(g)
