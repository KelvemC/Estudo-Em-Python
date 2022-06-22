numeroInt = 5
"""
while numeroInt >0:
    print(numeroInt)
    numeroInt-=1
"""
def reduzir_numero(numero):
    if numero>0:
        print(f"{numero} ({numero+1} - 1)" if (numero <5) else (numero))
        reduzir_numero(numero-1) 
        #Se eu utilizar o print nessa linha 11, ele vai printar os valores devolvidos da minha função,
        #sempre que uso uma função ela vai devolver se existir um valor, tudo que foi feito dentro foi a ida mas também tem a volta
    

#reduzir_numero(numero=5)

"""
1 - checar se o número não é igual a 0
2 - se ele não for igual a 0 - reduzir 1 unidade

5(N - 1)
    4 (5 - 1)
        3  (4 - 1)
            2  (3 - 1)
                1 (2 - 1)
"""

#Fatorial sem recursão
def fatorialS(numero):
    fatorial = 1
    if(numero) == 0:
        return 1
    elif(numero<0):
        return"Não existe fatorial de número negativo"
    else:
        for x in range(1,numero+1):
            fatorial*=x
        return fatorial

#Fatorial solução recursiva
def fatorial_r(numero):
    if(numero<0): return "Não existe fatorial de número negativo!"
    elif (numero ==0): return 1 #Critério de parada
    else: return numero * fatorial_r(numero-1) # Parâmetro da chamada recursiva
        
print(fatorial_r(3))
"""
3! = 3*!2
   = 3*2*!1
"""