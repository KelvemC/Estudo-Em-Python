from random import choice

jogador_vitorias = 0
maquina_vitorias = 0


def Opcao_Jogador():
    
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra": return esc_jogador
    elif esc_jogador == "papel": return esc_jogador
    elif esc_jogador == "tesoura": return esc_jogador
    else: print("Opção inválida. Tente novamente!"); Opcao_Jogador()

def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel","tesoura"])#função que escolhe uma das opções da lista
    return esc_maquina


while True:
    
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina() 
    esc_jogador = input("Você quer jogar novamente?")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["NÃO", "não", "NAO","nao", "Nao", "n", "N"]:
        break
    else:
        break 

