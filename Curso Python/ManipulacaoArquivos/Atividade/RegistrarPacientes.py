import os
from datetime import date, datetime

def registrar_paciente():
    loop = True
    while loop == True:
        nome_paciente = input('Insira o nome completo: ')
        email = input('Insira o e-mail do paciente: ')
        cpf= int(input('Insira o cpf do paciente: '))
        rg = int(input('Insira o rg do paciente: '))
        telefone = int(input('Insira o telefone do paciente: '))
        data_nascimento = input('Insira a data de nasicmento do paciente DD/MM/AAAA: ')
        
        data = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        ano_atual = date.today().year
        idade = ano_atual-data.year

        if(idade>=65):
            with open('Registro.txt','a') as arquivo:
                arquivo.write(f"Paciente: {nome_paciente}, pertence ao Grupo de Risco")
                arquivo.write(f"\nEmail: {email} \nCPF: {cpf} \nRG: {rg}")
                arquivo.write(f"\nTEL: {telefone} \nNascimento: {data_nascimento} \nIdade: {idade}\n")
                arquivo.write('\n')
        else:
            with open('Registro.txt','a') as arquivo:
                arquivo.write(f"Paciente: {nome_paciente}")
                arquivo.write(f"\nEmail: {email} \nCPF: {cpf} \nRG: {rg}")
                arquivo.write(f"\nTEL: {telefone} \nNascimento: {data_nascimento} \nIdade: {idade}\n")
                arquivo.write('\n')

        with open('Registro.txt', 'r') as arquivo:
            arquivo.read()
        
        solicitacao = input('Deseja registrar um novo paciente (S/N)?')
        if(solicitacao in ['S','s','Sim']):
            pass
        else:
            break

if __name__ =='__main__':
    registrar_paciente()
