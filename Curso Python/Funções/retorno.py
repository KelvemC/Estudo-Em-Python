lista = [1,2,3,4,5]
print(lista)

#Avaliando a função para saber se ela retorna algo
retorno = lista.pop()
var1 = print("Hello World")
print(var1) #none sem retorno
print("Retorno da função pop:", retorno)
"""
def ola_mundo():
    print("olá mundo")

retorno = ola_mundo();
print(retorno)


#definindo o retorno de uma função:
def ola_mundo():
    return "Olá mundo!"

var1 = ola_mundo()
print(var1)
#porem se eu chamar apenas minha função, o "ola mundo" não será impresso no terminal
"""
def par_impar():
    numero = 23
    if(numero%2 == 0):
        return "é par"
    else:
        return "é impar"
#quando utilizamos return além dele nos retornar a string ele sai da função, se tiver mais algo abaixo dele
#não vai ser executado.
print(par_impar())