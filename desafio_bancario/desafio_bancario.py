from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[92m',
         'amarelo':'\033[93m',
         'azul':'\033[34m',
         'ciano':'\033[96m'}

def ler_dinheiro(mensagem):
    valor_valido = False
    while not valor_valido:
        valor = str(input(mensagem).strip().replace(',','.'))
        try:
            valor = float(valor)
            valor_valido = True
            return valor
        except ValueError:
            print('Valor inválido, tente novamente.')
           
def ler_numero_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except(ValueError, TypeError):
            print(f'Operação inválida, tente novamente.')
        else:
            if 0 <= numero <= 3:
                return numero
            else:
                print('Operação inválida, tente novamente')
            
def cabecalho(mensagem):
    print(f'{cores['ciano']}~{cores['limpa']}' * 30)
    print(f'{cores['ciano']}{mensagem:^30}{cores['limpa']}')
    print(f'{cores['ciano']}~{cores['limpa']}' * 30)

def exibir_extrato(dicionario):
    cabecalho('EXTRATO')
    for keys, values in dicionario.items():
        print(f'{keys:.<15}{values:.>15}\n')

def menu():
    cabecalho('Banco DIO Suzano')
    print(f'{cores['amarelo']}[1]{cores['limpa']} - {cores['verde']}Depósito{cores['limpa']}')
    print(f'{cores['amarelo']}[2]{cores['limpa']} - {cores['vermelho']}Saque{cores['limpa']}')
    print(f'{cores['amarelo']}[3]{cores['limpa']} - {cores['azul']}Extrato{cores['limpa']}')
    print(f'{cores['amarelo']}[0]{cores['limpa']} - Sair')
    print(f'{cores['ciano']}~{cores['limpa']}' * 30)
    opcao = ler_numero_inteiro(f'{cores['amarelo']}Digite a operação: {cores['limpa']}')
    return opcao

quantidade_saque = quantidade_deposito = saque = deposito = saldo = opcao = 0
limite_saque = 3
extrato = {}
operacao = {}

while True:
    opcao = menu()
    if opcao == 1:
        deposito = ler_dinheiro('Valor do depósito: R$')
        if deposito > 0:
            saldo += deposito
            quantidade_deposito += 1
            operacao[f'Depósito {quantidade_deposito}'] = f'R${deposito:.2f}'
            extrato = extrato | operacao
            operacao.clear()        
            print('Depósito realizado com sucesso!')
            sleep(1.5)
        else:
            print('Valor inválido, tente novamente.')
            sleep(1.5)
    if opcao == 2:
        print('Limite por saque: R$500,00')
        print(f'Saques disponíveis: {limite_saque}')
        saque = ler_dinheiro('Valor do saque: R$')
        if saque > 0:
            if limite_saque == 0:
                print('Limite de saques diários excedido, tente novamente amanhã.')
                sleep(1.5)
                continue
            elif saque > 500.00:
                print('Saque acima do limite, tente novamente.')
                sleep(1.5)
            elif saque > saldo:
                print('Saldo insuficiente, consulte o extrato.')
                sleep(1.5)
                continue
            elif saque <= 500.00:
                saldo -= saque
                limite_saque -= 1
                quantidade_saque += 1
                operacao[f'Saque {quantidade_saque}'] = f'R${saque:.2f}'
                extrato = extrato | operacao
                operacao.clear()
                print('Saque realizado com sucesso! Retire o dinheiro.')
                sleep(1.5)
            else:
                print('Operação inválida, tente novamente.')
                sleep(1.5)
        else:
            print('Valor inválido, tente novamente.')
            sleep(1.5)
    if opcao == 3:
        exibir_extrato(extrato)
        print(f'Saldo: R${saldo:.2f}')
        sleep(3)             
    if opcao == 0:
        print('Encerrando operações. Obrigado por escolher o BDS!')
        sleep(1.5)
        break
