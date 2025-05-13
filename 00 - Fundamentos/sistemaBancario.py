from datetime import datetime

def menu():
    print("\n" + "="*40)
    print("         SISTEMA BANCÁRIO")
    print("="*40)
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Criar Usuário")
    print("5 - Criar Conta Corrente")
    print("6 - Listar Cadastros")
    print("7 - Sair")
    print("="*40)
    return input("Escolha uma opção (1-7): ")

def depositar(saldo, valor, extrato, /):
    print("\n" + "="*40)
    print("         DEPÓSITO")
    print("="*40)
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: Valor inválido para depósito. Deve ser positivo.")
    print("="*40)
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print("\n" + "="*40)
    print("         SAQUE")
    print("="*40)
    if numero_saques >= limite_saques:
        print(f"Erro: Limite de saques diários atingido ({limite_saques} saques).")
    elif valor > saldo:
        print("Erro: Saldo insuficiente para o saque.")
    elif valor > limite:
        print(f"Erro: Limite máximo por saque é de R$ {limite:.2f}.")
    elif valor <= 0:
        print("Erro: Valor inválido para saque. Deve ser positivo.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Saque:    R$ {valor:.2f}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saques restantes: {limite_saques - numero_saques}")
        return saldo, extrato, numero_saques
    print("="*40)
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n" + "="*40)
    print("         EXTRATO")
    print("="*40)
    print("Histórico de Transações:")
    print("-"*40)
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print("-"*40)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("="*40)

def criar_usuario(usuarios):
    print("\n" + "="*40)
    print("         CRIAR USUÁRIO")
    print("="*40)
    cpf = input("Informe o CPF (somente números): ")
    if not cpf.isdigit():
        print("Erro: CPF inválido. Deve conter apenas números.")
        print("="*40)
        return usuarios
    
    cpf = int(cpf)
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Erro: CPF já cadastrado.")
        print("="*40)
        return usuarios
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade, estado): ")
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")
    print("="*40)
    return usuarios

def criar_conta_corrente(contas, usuarios):
    print("\n" + "="*40)
    print("         CRIAR CONTA CORRENTE")
    print("="*40)
    cpf = input("Informe o CPF do usuário (somente números): ")
    if not cpf.isdigit():
        print("Erro: CPF inválido. Deve conter apenas números.")
        print("="*40)
        return contas
    
    cpf = int(cpf)
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Erro: Usuário com este CPF não encontrado.")
        print("="*40)
        return contas
    
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta corrente {numero_conta} (Agência: 0001) criada com sucesso para {usuario['nome']}!")
    print("="*40)
    return contas

def listar_cadastros(usuarios, contas):
    print("\n" + "="*40)
    print("         LISTAR CADASTROS")
    print("="*40)
    
    print("\nUSUÁRIOS CADASTRADOS:")
    print("-"*40)
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"Endereço: {usuario['endereco']}")
            print("-"*40)
    
    print("\nCONTAS CADASTRADAS:")
    print("-"*40)
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Usuário: {conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})")
            print("-"*40)
    
    print("="*40)

# Variáveis do sistema bancário
saldo = 0.0
extrato = ""
limite_saque = 500.00
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

# Loop principal
while True:
    opcao = menu()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        except ValueError:
            print("\n" + "="*40)
            print("Erro: Entrada inválida. Digite um valor numérico.")
            print("="*40)

    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        except ValueError:
            print("\n" + "="*40)
            print("Erro: Entrada inválida. Digite um valor numérico.")
            print("="*40)

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        usuarios = criar_usuario(usuarios)

    elif opcao == "5":
        contas = criar_conta_corrente(contas, usuarios)

    elif opcao == "6":
        listar_cadastros(usuarios, contas)

    elif opcao == "7":
        print("\n" + "="*40)
        print("Obrigado por utilizar o sistema bancário!")
        print("="*40)
        break

    else:
        print("\n" + "="*40)
        print("Erro: Opção inválida. Escolha um número entre 1 e 7.")
        print("="*40)
