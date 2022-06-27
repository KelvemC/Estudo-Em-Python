"""
    Esse módulo tem como objetivo:
        retornar se um número que é passado como parâmetro é 
        ou não primo.
    
    Funções disponíveis:
        primo
"""
def primo(numero):
    """
        Essa função recebe como parâmetro um número,
        verifica se ele é maior que 1 e me retorna se é primo ou
        não.

        Parâmetros (numero):
            1 parâmetro obrigatório - do tipo inteiro
    """
    if numero > 1:
        #Verificando resto das divisões
        for x in range(2, numero):
            if(numero % x) == 0:
                return "Esse não é um número primo"
        else:
            return "Esse número é primo"
    else:
        return "Esse número não é primo: número menor ou igual a 1"

#O dunder name vai receber o nome do arquivo, e se ele estiver sendo execultado diretamente, se ele for o modulo principal de execução, ele vai mostrar somente o print
if __name__ == "__main__":
    print(primo(5))
