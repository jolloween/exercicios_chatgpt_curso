# Projeto: Sistema de Gerenciamento de Funcionários
# Descrição

# Você vai criar um sistema simples para gerenciar informações de
# funcionários de uma empresa. O sistema deve permitir:

# Adicionar funcionários (nome, idade, salário).

# Listar todos os funcionários.

# Buscar um funcionário pelo nome.

# Atualizar salário de um funcionário.

# Remover um funcionário.

# Exibir funcionários com salário acima de um valor informado.

# Sair do sistema.
import os
import json
import time
def salvar_dados(funcionarios, arquivo="funcionarios.json"):
    """Salva o dicionário de funcionários em um arquivo JSON"""
    with open(arquivo, "w") as f:
        json.dump(funcionarios, f, indent=4)

def carregar_dados(arquivo="funcionarios.json"):
    """Carrega os funcionários do arquivo JSON"""
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastrar_funcionário(funcionários):
    nome = input("Nome do funcionário: ").title()
    if nome in funcionários:
        print("Funcionário já existe.")
    funcionários[nome] = {}
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("⚠️ Digite uma idade válida.")
            continue
    while True:
        try:
            salario = int(input("Salário: "))
            break
        except ValueError:
            print("⚠️ Sálario inválido.")
            continue

    dados = {'idade': idade, 'salário': salario}
    funcionários[nome] = dados
    salvar_dados(funcionários)
    print(f"👌  Funcionário {nome} cadastrado com sucesso!")
    input("\nCarregue enter para continuar...")

def listar_funcionários(funcionários):
    if not funcionários:
        print("Não há funcionários cadastrados")
        print("---"*20)
    for nome in sorted(funcionários):
        dados = funcionários[nome]
        print(f"Nome: {nome:<17} | Idade: {dados['idade']:^5} | Salário: ${dados['salário']:>8.2f}")
        print("---"*20)

    input("\nCarregue enter para continuar...")

def buscar_funcionarios(funcionários):
    nome = input("Nome do funcionário: ").title()

    if nome in funcionários:
        print(f"Nome: {nome}  |  Idade: {funcionários[nome]['idade']}  |  Salário: ${funcionários[nome]['salário']}")
        input("\nDigite enter para continuar...")
    else:
        print(f"{nome} não consta na lista de funcionários.")
        input("\nCarregue enter para continuar...")

def atualizar_salario(funcionários):
    listar_funcionários(funcionários)
    nome = input("Qual Funcionário desejas alterar o salário: ")
    if nome in funcionários:
        while True:
            try:
                novo_salario = float(input(f"Novo salário de {nome}: $"))
                funcionários[nome]['salário'] = novo_salario
                print(f"novo salário de {nome}: ${novo_salario:.2f}")
                salvar_dados(funcionários)
                input("\nCarregue enter para sair...")
                break
            except ValueError:
                print("Digite um salário válido.")
                continue
    else:
        print(f"❌  {nome} não consta na lista de fucionários")
        input("\nCarregue enter para continuar...")

def remover_funcionario(funcionários):
    listar_funcionários(funcionários)
    nome = input("Digite o funcionário que desejas remover: ").title().strip()
    if nome in funcionários:
        while True:
            # escolha = input(f"Tem certeza que deseja remover {nome}")
            if input(f"Tem certeza que deseja remover {nome}? [S/N]").strip().upper() == 'S':
                del funcionários[nome]
                print(f"Funcionário {nome} removido com sucesso!")
                salvar_dados(funcionários)
                input("\nCarregue enter para continuar...")
                break
            else:
                print("Operação cancelada com sucesso!")
                break
    else:
        print(f"{nome} não consta na lista de funcionários.")
        input("\nCarregue enter para continuar...")
def salario_acima_x(funcionários):
    limpar_tela()
    while True:
        try:
            valor = float(input("Informe o valor mínimo do salário (R$): "))
            break
        except ValueError:
            print("❌  Valor inválido.")
            continue

    encontrados = False
    for nome, dados in funcionários.items():
        if dados['salário'] > valor:
            print(f"{nome:<20} | R$ {dados['salário']:>10.2f}")
            encontrados = True
    if not encontrados:
        print("Nenhum funcionário encontrado com salário acima desse valor.")
        encontrados = False
    input("\nCarregue ENTER para sair...")
def menu():
    print("=-"*20)
    print(f"{'MENU':^40}")
    print("=-"*20)
    print('[1] Adicionar funcionários')
    print('[2] listar funcionários')
    print('[3] Buscar funcionário')
    print('[4] Atualizar salário')
    print('[5] Remover funcionário')
    print('[6] pesquisa por salários')
    print('[7] Sair')
limpar_tela()

funcionários = carregar_dados()

# PROGRAMA PRINCIPAL
while True:
    limpar_tela()
    menu()
    try:
        opção = int(input("Escolha sua opção: "))
        if opção < 1 or opção > 7:
            print("⚠️  Opção inválida")
            input("\nCarregue ENTER para contnuar...")
            continue

    except ValueError:
        print("⚠️  Opção inválida")
        input("\nCarregue ENTER para continuar..")
        continue

    if opção == 1:
        cadastrar_funcionário(funcionários)
    elif opção == 2:
        listar_funcionários(funcionários)
    elif opção == 3:
        buscar_funcionarios(funcionários)
    elif opção == 4:
        atualizar_salario(funcionários)
    elif opção == 5:
        remover_funcionario(funcionários)
    elif opção == 6:
        salario_acima_x(funcionários)
    else:
        print("Encerrando programa...")
        for i in range(3, 0, -1):
            print(i, end="... ")
            time.sleep(1)
        print("❌",end="")
        print("\nPrograma encerrado com sucesso!")
        break
    # if input("Quer continuar? [S/N]").strip().upper() == 'N':
    #     break


