from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[92m',
         'amarelo':'\033[93m',
         'azul':'\033[34m',
         'ciano':'\033[96m'}

def ler_nome(mensagem):
    nome_valido = False
    while not nome_valido:
        nome = str(input(mensagem).strip())
        try:
            if nome.isalpha() == True:
                return nome
        except TypeError:
            print('Nome inválido, tente novamente.')

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
            if 0 <= numero <= 6:
                return numero
            else:
                print('Operação inválida, tente novamente')
            
def cabecalho(mensagem):
    print(f'{cores['ciano']}~{cores['limpa']}' * 30)
    print(f'{cores['ciano']}{mensagem:^30}{cores['limpa']}')
    print(f'{cores['ciano']}~{cores['limpa']}' * 30)

def exibir_extrato(saldo, /, *, extrato):
    cabecalho('EXTRATO')
    for keys, values in extrato.items():
        print(f'{keys:.<15}{values:.>15}\n')
    print(f'Saldo: R${saldo:.2f}')
    sleep(3)

def menu():
    cabecalho('Banco DIO Suzano')
    print(f'{cores['amarelo']}[1]{cores['limpa']} - {cores['verde']}Depósito{cores['limpa']}')
    print(f'{cores['amarelo']}[2]{cores['limpa']} - {cores['vermelho']}Saque{cores['limpa']}')
    print(f'{cores['amarelo']}[3]{cores['limpa']} - {cores['azul']}Extrato{cores['limpa']}')
    print(f'{cores['amarelo']}[4]{cores['limpa']} - Novo usuário')
    print(f'{cores['amarelo']}[5]{cores['limpa']} - Nova conta')
    print(f'{cores['amarelo']}[6]{cores['limpa']} - Ver contas')
    print(f'{cores['amarelo']}[0]{cores['limpa']} - Sair')
    print(f'{cores['ciano']}~{cores['limpa']}' * 30)
    opcao = ler_numero_inteiro(f'{cores['amarelo']}Digite a operação: {cores['limpa']}')
    return opcao

def depositar(saldo, deposito, extrato, quantidade_deposito, /):
    if deposito > 0:
        saldo += deposito
        quantidade_deposito += 1
        extrato[f'Depósito {quantidade_deposito}'] = f'R${deposito:.2f}'            
        print('Depósito realizado com sucesso!')
        sleep(1.5)
    else:
        print('Valor inválido, tente novamente.')
        sleep(1.5)
    return saldo, extrato, quantidade_deposito

def sacar(*, saldo, saque, extrato, limite_saque, quantidade_saque):
    if saque > 0:
        if limite_saque == 0:
            print('Limite de saques diários excedido, tente novamente amanhã.')
            sleep(1.5)
        elif saque > 500.00:
            print('Saque acima do limite, tente novamente.')
            sleep(1.5)
        elif saque > saldo:
            print('Saldo insuficiente, consulte o extrato.')
            sleep(1.5)
        elif saque <= 500.00:
            saldo -= saque
            limite_saque -= 1
            quantidade_saque += 1
            extrato[f'Saque {quantidade_saque}'] = f'R${saque:.2f}'
            print('Saque realizado com sucesso! Retire o dinheiro.')
            sleep(1.5)
        else:
            print('Operação inválida, tente novamente.')
            sleep(1.5)
    else:
        print('Valor inválido, tente novamente.')
        sleep(1.5)
    return saldo, extrato, limite_saque, quantidade_saque

def encontrar_usuario(cpf, usuarios):
    usuario_encontrado = False
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            usuario_encontrado = True
            break
    return usuario_encontrado

def usuario(usuarios):
    cpf = input('Digite seu CPF (apenas números): ').strip()
    if cpf.isnumeric() and len(cpf) == 11:
        usuario_existente = encontrar_usuario(cpf, usuarios)
        if usuario_existente == False:
            nome = str(input('Digite seu nome completo: ').strip())
            data_nascimento = str(input('Digite sua data de nascimento [dd/mm/aaaa]: ').strip())
            endereco = str(input('Digite seu endereço [Logradouro, nº - Bairro - Cidade/Sigla Estado]: ').strip())
            usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
            print('Usuário criado com sucesso!')
            sleep(1.5)
        else:
            print('Já existe um usuário com o CPF informado.')
            sleep(1.5)
    else:
        print('CPF inválido, tente novamente.')
        sleep(1.5)
   
def conta(agencia, numero_conta, usuarios, contas):
    cpf = input('Digite seu CPF (apenas números): ').strip()
    if cpf.isnumeric() and len(cpf) == 11:
        usuario_encontrado = encontrar_usuario(cpf, usuarios)
        if usuario_encontrado == True:
            numero_conta += 1
            contas.append({'usuario': cpf, 'agencia': agencia, 'numero_conta': numero_conta})
            print('Conta criada com sucesso!')
            print(f'Usuário: {cpf}\nAgência: {agencia}\nConta Corrente: {numero_conta}')
            sleep(1.5)
        else:
            print('CPF não cadastrado, crie um novo usuário.')
            sleep(1.5)
    else:
        print('CPF inválido, tente novamente.')
        sleep(1.5) 
    return numero_conta       

def listar_contas(contas):
    cpf = input('Digite seu CPF (apenas números): ').strip()
    if cpf.isnumeric() and len(cpf) == 11:
        conta_encontrada = False
        for conta in contas:
            if cpf == conta['usuario']:
                conta_encontrada = True
                break
        if conta_encontrada == True:
                cabecalho(f'Usuário: {cpf}')
                for conta in contas:
                    if cpf == conta['usuario']:
                        print(f'Ag: {conta['agencia']}\nC/c: {conta['numero_conta']}\n{'~' * 30}')
        else:
            print('Não existem contas vinculadas ao CPF informado.')
        sleep(1.5)
    else:
        print('CPF inválido, tente novamente.')
        sleep(1.5)

AGENCIA = '0001'
quantidade_deposito = quantidade_saque = numero_conta = saque = deposito = saldo = opcao = 0
limite_saque = 3
extrato = {}
usuarios = []
contas = []

while True:
    opcao = menu()
    if opcao == 1:
        deposito = ler_dinheiro('Valor do depósito: R$')
        saldo, extrato, quantidade_deposito = depositar(saldo, deposito, extrato, quantidade_deposito)
    if opcao == 2:
        print('Limite por saque: R$500,00')
        print(f'Saques disponíveis: {limite_saque}')
        saque = ler_dinheiro('Valor do saque: R$')
        saldo, extrato, limite_saque, quantidade_saque = sacar(
            saldo=saldo,
            saque=saque,
            extrato=extrato,
            limite_saque=limite_saque,
            quantidade_saque=quantidade_saque
        )
    if opcao == 3:
        exibir_extrato(saldo, extrato=extrato)
    if opcao == 4:
        usuario(usuarios)    
    if opcao == 5:
        numero_conta = conta(AGENCIA, numero_conta, usuarios, contas)    
    if opcao == 6:
        listar_contas(contas)    
    if opcao == 0:
        print('Encerrando operações. Obrigado por escolher o BDS!')
        sleep(1.5)
        break
