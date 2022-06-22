#Parâmetros de uma função

def minha_funcao():
    var = "Kelvem"
    return var #retornando o valor, não a variável

var = minha_funcao() #Fazendo a variável var armazenar o valor retornado do 'var' da minha_funcao

def imprime_nome(nome, sobrenome, idade): #Parâmetro é um nome dado aos valores utilizados na definição de uma função
    #corpo da função
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)
    

nome = input("Qual é o seu nome?")
sobrenome = input("Qual é o seu sobrenome?")
idade = int(input("Quantos anos você tem?"))
imprime_nome(nome, sobrenome, idade) #argumento é o nome dado aos valores utilizados na chamada de uma função
