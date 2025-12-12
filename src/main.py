from utils.users import *
from utils.functions import *
from datetime import datetime as dt, timedelta as tdelta, date

titulo = ' Bem vindo ao Banco Piton '
slogan = 'Seu banco de confiança!'
print(titulo.center(50, '~'))
print(slogan.center(50, ' ') + '\n')

LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.00

saques = 0
menu = '''
=== Menu ===
D = Depositar
S = Sacar
E = Extrato
Q = Sair
'''
agencia = input('Digite sua agência: ')
conta = input('Digite sua conta: ')

if (validar_conta(agencia, conta) == True):
    if (validar_senha(agencia, conta) == True):
        while True:
            print(menu)
            escolha = input('O que deseja fazer? ')

            if (escolha.upper() == 'D'):
                try:
                    deposito = float(input('\nDigite o valor do depósito: R$'))
                    agencias[agencia][conta]["saldo"] += deposito
                    agencias[agencia][conta]["extrato"].setdefault(f'{dt.now()}', f'Depósito: R${deposito}')
                    print(f'Depósito realizado com sucesso!')
                    print(f'\nSeu saldo atual é de {agencias[agencia][conta]["moeda"]}{agencias[agencia][conta]["saldo"]}')

                except ValueError:
                    print('Por favor digite apenas números e pontos para valores com casas decimais.')
            
            elif (escolha.upper() == 'S'):
                if (saques == LIMITE_SAQUES):
                    print(f'O número máximo de saques diários(3) foi atingido, por favor espere até {date.today() + tdelta(days=1)} ou realize outra operação.')
                else:
                    try:
                        saque = float(input('\nDigite o valor do saque: R$'))
                        if (saque > LIMITE_POR_SAQUE):
                            print('Saque excede o limite por saque(R$500,00), por favor tente novamente.')
                        elif saque > agencias[agencia][conta]["saldo"]:
                                print('Saldo insuficiente, tente novamente.')
                        else:
                            saques += 1
                            agencias[agencia][conta]["saldo"] -= saque
                            agencias[agencia][conta]["extrato"].setdefault(f'{dt.now()}', f'Saque: R${saque}')
                            print(f'Saque realizado com sucesso!\n')
                            print(f'Seu saldo atual é de {agencias[agencia][conta]["moeda"]}{agencias[agencia][conta]["saldo"]}')

                    except ValueError:
                        print('Por favor digite apenas números e pontos para valores com casas decimais.')
                
            elif (escolha.upper() == 'E'):
                print(f'''
=== EXTRATO ===

{agencias[agencia][conta]["extrato"]}
            
Seu saldo atual é de: R$ {agencias[agencia][conta]["saldo"]}'
===============
''')
            
            elif (escolha.upper() == 'Q'):
                print('\nObrigado por usar o Banco Piton. Volte sempre!')
                break

            else:
                 print('\nPor favor digite uma opção válida.')