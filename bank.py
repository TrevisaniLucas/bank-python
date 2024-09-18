menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":  # OPCAO DEPOSITO
        deposito = float(input("Digite o valor do depósito: "))  # DEPOSITO
        
        if deposito > 0:  # VALIDACAO DO DEPOSITO
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("A operação falhou! Valor inválido.")

    elif opcao == "s":  # OPCAO SAQUE
        valor = float(input("Digite o valor que deseja sacar: "))  # SAQUE

        if valor > saldo:
            print("Saque maior que o saldo.")
        elif valor > limite:
            print("O valor do saque excede o limite permitido.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":  # OPCAO EXTRATO
        print("\n=========== Extrato ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":  # OPCAO SAIR
        break

    else:
        print("Operação inválida, por favor selecione novamente.")
