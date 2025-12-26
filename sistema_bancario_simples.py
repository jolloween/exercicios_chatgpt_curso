# 9. Sistema Bancário Simples

# Contas {numero: saldo}

# Função para depósito e saque.

# Verificar saldo insuficiente.

import os

def menu_banco():
    print("BANCO ON-LINE")
    print("[1] depósito")
    print("[2] saque")
    print("[3] listar saldo das contas")
    print("[0] sair")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def conta_saldo():
    for k, v in contas.items():
        print(f"Conta: {k} Saldo: ${v:.2f}")

def deposito_saque_saldo(contas, opção):
    if opção == 1:
        conta_saldo()
        conta = int(input("Digite a conta que desejas fazer o depósito: "))
        if conta not in contas:
            print(f"Conta: {conta} inexistente.")
        else:
            valor = float(input("valor do depósito: "))
            contas[conta] += valor
            print(f"Depósito de ${valor:.2f} efetuado com sucesso.")
            print(f"Novo saldo é de ${contas[conta]:.2f}")
    elif opção == 2:
        conta_saldo()
        conta = int(input("Digite a conta que desejas fazer o saque: "))
        if conta not in contas:
            print(f"Conta: {conta} inexistente.")
        else:
            valor = float(input("valor do saque: "))
            if valor > contas[conta]:
                print("valor insuficiente")
            else:
                contas[conta] -= valor
                print(f"Saque realizado. Saldo atual: ${contas[conta]:.2f}")

    elif opção == 3:
        conta_saldo()
    
        
#PROGRAMA PRINCIPAL
limpar_tela()

contas = {
    1001: 1500.00,
    1002: 800.00,
    1003: 250.00
}

while True:
    menu_banco()
    opção = int(input("escolha sua opção (0 para sair): "))

    if opção == 0:
        break
    
    deposito_saque_saldo(contas, opção)

    input("\nPressione Enter para continuar...")  # Pausa antes de limpar
    limpar_tela()

limpar_tela()
print("=-" *15)
print("      saldo atualizado")
print("=-" *15)
for k, v in contas.items():
    print(f"Conta: {k} Saldo: ${v:.2f}")
print("=-" *15)