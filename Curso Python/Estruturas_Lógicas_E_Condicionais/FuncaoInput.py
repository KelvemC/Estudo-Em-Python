"""
Função input() - função que serve para ler dados do teclado.
A função input recebe como parâmetro uma string que será mostrada como auxílio ao usuário, 
geralmente o informando que tipo de dado o programa está aguardando receber.
"""
#1° Forma
print("Insira um nome: ")
nome = input()

print("Agora insira um dado para saber o tipo: ")
dado = input()
print(type(dado))

#2° Forma

nome = input("Insira um nome: ")
dado = input("Agora insira um dado para saber o tipo: ")
print(f"Seu nome é {nome} e seu tipo de dado é {type(dado)}")
