#variável global e local

x = 5
print("O valor da variável global é",x)

def funcao():
    x = 3
    print("O valor da variável local é", x)

funcao()