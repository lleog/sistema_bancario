menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 600
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informa quanto vai botar. Lá ele kkkkk: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente. Trabalhe para ter dinheiro '-' ") 

        elif excedeu_limite:
            print("O valor do saque excede o limite de saque! Tu é burro ou se faz?? ")

        elif excedeu_saques:
            print("Você já retirou o dinheiro 3 vezes! TENTE MAIS AMANHÃ!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Digite o comando certo para não da erro! Seu lesado!")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Sem movimentação. Pobre kkkk" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Se ficar de gracinha vou te mandar lá para aquela casa irmão")