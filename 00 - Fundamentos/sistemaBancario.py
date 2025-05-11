def menu():
    print("\n====== MENU ======")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    return input("Escolha uma opção: ")

# Variáveis do sistema bancário
saldo = 0.0
extrato = ""
limite_saque = 500.00
saques_realizados = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    opcao = menu()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        if saques_realizados >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
            continue

        valor = float(input("Informe o valor do saque: R$ "))
        if valor > saldo:
            print("Saldo insuficiente para o saque.")
        elif valor > limite_saque:
            print("Limite máximo por saque é de R$ 500.00.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor
            saques_realizados += 1
            extrato += f"Saque:    R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == "3":
        print("\n====== EXTRATO ======")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por utilizar o sistema bancário.")
        break

    else:
        print("Opção inválida. Escolha novamente.")
