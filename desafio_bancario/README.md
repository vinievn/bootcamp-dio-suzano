# Objetivo
- Criar um sistema bancário simples com as operações: **sacar**, **depositar**, **extrato**, criar **usuário** e **conta bancária**;
- Limite de 10 transações por dia.
## Depósito
- Apenas valores positivos;
- Armazenado em variável;
- Definido em uma função;
  - Positional only.
- Exibido na opção de **extrato**.
## Saque
- Limite de 03 saques diários;
- Limite de R$500,00 por saque;
- Retornar mensagem de saque inválido;
- Armazenado em variável;
- Definido em uma função;
  - Keyword only.
- Exibido na opção de **extrato**.
## Extrato
- Saldo começa zerado;
- Listar todos os **depósitos** e **saques**;
- Exibir o saldo atual da conta;
- Exibir valores formatados em: R$ X,XX;
- Definido em uma função;
  - Positional only: saldo.
  - Keyword only: extrato.
- Exibir data e hora de todas as transações.
## Criar usuário (cliente)
- Armazenado em lista;
- Deve conter: nome, data de nascimento, CPF e endereço;
- Endereço deve ser uma str no formato: logradouro, número - bairro - cidade/sigla do estado;
- CPF: limite de um usuário por CPF, armazenar apenas números.
## Criar conta bancária
- Armazenado em lista;
- Composta por: agência, número da conta e usuário;
- Agência: fixo em 0001;
- Número da conta: sequencial
- Usuário: pode ter múltiplas contas.
