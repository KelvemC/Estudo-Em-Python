from math import sqrt
def menu():
    """
        Função menu:
            Esta função serve para exibir o menu para o usuário
            pode ver todas as opções disponíveis.
    """
    return """
    -------------------------
    ==========MENU===========
    ( 1 ) = %
    ( 2 ) = 1/x
    ( 3 ) = x²
    ( 4 ) = ²√X
    ( 5 ) = ÷
    ( 6 ) = x
    ( 7 ) = -
    ( 8 ) = +
    ( 9 ) = +/-
    =========================
    """
    

def escolha():
    """
        Função escolha menu:
            Esta função complementa a do menu, após verificar qual das
            opções deseja escolher, poderá digitar pelo teclado o número,
            esse número será salvo e utilizado pelas outras funções.

        # Digito um valor, ele será salvo e depois retornado.
    """
    esc = (input("Escolha uma das opções do Menu: "))
    return esc


def modulo():
    """
        Função calculo modulo:
            Esta função serve para calcular o modulo entre dois números
            
            As variáveis numero1 e numero2 vão receber os dados pelo teclado
            E de acordo com os números recebidos será feito o calculo do módulo entre eles.

            # Exemplo: Numero1 = 7.55 e Numero2 = 8.80
            # return (7.55/100) * 8.80
    """
    
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return (numero1/100) * numero2
    

def inverso_numero():
    """
        Função inverso do número:
            Esta função serve para retornar o inverso de um número
            Um número multiplicado pelo seu inverso é igual a 1. 
            Todos os números reais diferentes de 0 têm um inverso
            
            # Exemplo: o inverso de 5 é 1/5
    """
    
    numero = float(input("Insira um valor: "))
    if numero != 0:
        return f"O inverso de {numero} é 1/{numero}"
    else:
        return "Não existe inverso de um número igual a 0 ou menor" 
   

def potenciacao():
    """
        Função numero²:
            Esta função serve para retorna a potenciação de um número ao quadrado

            # Exemplo 5² é 25, que é o mesmo que 5 * 5
    """
    numero = float(input("Insira um valor: "))
    return numero**2
   

def raiz_Ao_quadrado():
    """
        Função raiz ao quadrado:
            Esta função serve para calcular a raiz quadrada de um número

            Para isso foi usado uma biblioteca padrão chamada math
            que disponibiliza funções matemáticas e nela tem a sqrt,
            que serve exatamente para calcular a raiz quadra, 
            nela devemos passar um número como parâmetro,

            # Exemplo sqrt(100) vai retornar a raiz quadrada de 100
    """
    numero1 = float(input("Insira o valor 1: "))
    return sqrt(numero1)


def divisao():
    """
        Função divisão:
            Esta função serve para retornar a divisão entre números

            # Exemplo numero1 = 565 e numero2 = 120
            # O retorno será 565/120 = 4,708333333
    """
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1/numero2


def multi():
    """
        Função Multiplicação:
            Esta função serve para retornar o multiplicação de um número

            # Exemplos 7*7 ele vai retornar 49
    """

    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1*numero2


def subtracao():
    """
        Função subtração:
            esta função serve para retornar a subtração entre dois números

            # Exemplo numero1 = 80 e numero2 = 50
            # 80-50 = 30 logo será retornado o valor 30
    """
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1-numero2


def soma():
    """
        Função soma:
            Esta função serve para retorna a soma entre dois números

            # Exemplo: numero1 = 5 e numero2 = 10
            # O retorno será 15, porque a soma de 5+10 = 15
    """
    numero1 = float(input("Insira o número 1: "))
    numero2 = float(input("Insira o número 2: "))
    return numero1+numero2


def nevativar():
    """
        Função negativar:
            Esta função serve para negativar um número

            # Exemplo a negativação de 500 é -500
            # Apos inserir o valor, a função vai retornar o valor inserido negativado
    """
    numero = float(input("Insira um valor: "))
    return -numero


def calculadora():
    print(menu())
    esc = escolha()
    
    if esc == '1': return modulo()
    elif esc == '2': return inverso_numero()
    elif esc == '3': return potenciacao()
    elif esc == '4': return raiz_Ao_quadrado()
    elif esc == '5': return divisao()
    elif esc == '6': return multi()
    elif esc == '7': return subtracao()
    elif esc == '8': return soma()
    elif esc == '9': return nevativar()
    else: print(f"\033[31mDigita uma opção correta\033[m"); return calculadora()
    
if __name__ == '__main__':
    print(calculadora())
    