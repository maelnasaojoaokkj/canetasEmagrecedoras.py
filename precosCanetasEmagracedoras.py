import os

mounjaro_2_5mg = 1884.31
mounjaro_5mg = 2355.61
mounjaro_7_5mg = 2766.26
mounjaro_10mg = 3210.85
mounjaro_12_5mg = 3765.44
mounjaro_15mg = 3765.44

ozempic_1mg = 1284.04
ozempic_1_34mg = 1284.04

wegovy_0_25mg = 1284.04
wegovy_0_5mg = 1284.04
wegovy_1mg = 1284.04
wegovy_1_7mg = 1923.36
wegovy_2_4mg = 2473.85

mou_page_num = 6
oze_page_num = 2
weg_page_num = 5

os.system('clear')


def mounjaro():
    print(
            '\n[1] 2_5MG \n'
            '[2] 5MG   \n'
            '[3] 7_5MG \n'
            '[4] 10MG  \n'
            '[5] 12_5MG\n'
            '[6] 15MG  \n'
            '[0] VOLTAR\n')

    m_input = input(
            'Comando: ').strip().lower()

    if m_input in ("1", "2_5mg") :
        os.system("clear")
        print(f'\nR$ {mounjaro_2_5mg:,.2f}\n')

    elif m_input in ("2", "5mg") :
        os.system("clear")
        print(f'\nR$ {mounjaro_5mg:,.2f}\n')

    elif m_input in ("3", "7_5mg") :
        os.system("clear")
        print(f'\nR$ {mounjaro_7_5mg:,.2f}\n')

    elif m_input in ("4", "10mg") :
        os.system("clear")
        print(f'\nR$ {mounjaro_10mg:,.2f}\n')

    elif m_input in ("5", "12_5mg") :
        os.system("clear")
        print(f'\nR$ {mounjaro_12_5mg:,.2f}\n')

    elif m_input in ("6", "15mg") :
        os.system("clear")
        print(f'\nR$ {mounjaro_15mg:,.2f}\n')

    elif m_input in ("0", "voltar") :
        os.system("clear")
        print("\nVoltando...")

def ozempic():
    print(
            '\n[1] 1MG\n'
            '[2] 1_34MG \n'
            '[0] VOLTAR\n')

    o_input = input(
            'Comando: ').strip().lower()

    if o_input in ("1", "1MG") :
        os.system('clear')
        print(f'\nR$ {ozempic_1mg:,.2f}\n')

    elif o_input in ('2', '1_34MG') :
        os.system('clear')
        print(f'\nR$ {ozempic_1_34mg:,.2f}\n')

    elif o_input in ('0', 'VOLTAR') :
        os.system('clear')
        print('\nVoltando...\n')

def wegovy():
    print(
            '\n[1] 0_25MG\n'
            '[2] 0_5MG\n'
            '[3] 1MG\n'
            '[4] 1_7MG\n'
            '[5] 2_4MG\n'
            '[0] VOLTAR\n'
            )

    w_input = input(
            'Comando: ').strip().lower()

    if w_input in ('1', "0_25MG\n"):
        os.system('clear')
        print(f'\nR$ {wegovy_0_25mg:,.2f}\n')

    elif w_input in ('2', '0_5MG') :
        os.system('clear')
        print(f'\nR$ {wegovy_0_5mg:,.2f}\n')

    elif w_input in ('3', '1_MG') :
        os.system('clear')
        print(f'\nR$ {wegovy_1mg:,.2f}\n')

    elif w_input in ('4', '1_07MG') :
        os.system('clear')
        print(f'\nR$ {wegovy_2_4mg:,.2f}\n')

    elif w_input in ('5', '2_4MG') :
        os.system('clear')
        print(f'\nR$ {wegovy_2_4mg:,.2f}\n')

    elif w_input in ('0', 'VOLTAR') :
        os.system('clear')
        print('\nVoltando...\n')

while True:
    user_input = input(
            '\nEscolha o medicamento:\n\n'
            '[1] MOUNJARO\n'
            '[2] OZEMPIC\n'
            '[3] WEGOVY\n'
            '[0] SAIR\n'
            '[*] LIMPAR\n\n'
            'Comando: '
            ).strip().lower()

    if user_input in ("mounjaro", "1") :
        mounjaro()

    elif user_input in ("ozempic", "2") :
        ozempic()

    elif user_input in ("wegovy", "3",) :
        wegovy()

    elif user_input == "" :
        print('\nVocê deve inserir o nome de um dos três medicamentos.\n')

    elif user_input in ("sair", "*") :
        os.system('clear')

    elif user_input in ("0", "sair") :
        print("\nPrograma encerrado.")
        break

    else:
        print(f'\n{user_input} não está entre as opções disponíveis.\n')
