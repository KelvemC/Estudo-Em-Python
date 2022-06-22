from random import choice

jogador_vitorias = 0
maquina_vitorias = 0


def Opcao_Jogador():
    
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra": return esc_jogador
    elif esc_jogador == "papel": return esc_jogador
    elif esc_jogador == "tesoura": return esc_jogador
    else: print("Opção inválida. Tente novamente!"); return Opcao_Jogador()

def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel","tesoura"])#função que escolhe uma das opções da lista
    return esc_maquina


while True:
    
    print('-'*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina() 
    print('-'*30)
    
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            #Jogador Ganha
            print(f"Jogador escolheu: {esc_jogador} e a máquina escolheu {esc_maquina}," 
            " Resultado: Você ganhou!")
            jogador_vitorias += 1 


    elif esc_jogador == esc_maquina:
        #Empate
        print(f"Jogador escolheu: {esc_jogador} e a máquina escolheu {esc_maquina}," 
            " Resultado: Empate!")
    
    
    else:
        #Máquina Ganha
        print(f"Jogador escolheu: {esc_jogador} e a máquina escolheu {esc_maquina}," 
            " Resultado: Você perdeu")
        maquina_vitorias += 1     
    
    
    #Uma linha de código deve ter no máximo 70 caracteres ou 80
    print('-'*30)
    print(f'Vitórias do jogador: {jogador_vitorias}')
    print(f'Vitórias da máquina: {maquina_vitorias}')
    print('-'*30)

    esc_jogador = input("Você quer jogar novamente?")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["NÃO", "não", "NAO","nao", "Nao", "n", "N"]:
        break
    else:
        break 

