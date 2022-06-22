#É preciso tomar cuidado com loops infinitos que não podemos controlar
def olamundo():
    print("Hello World!")
    olamundo()

def executar():
    olamundo()

executar()

