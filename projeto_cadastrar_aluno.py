# 📌 Projeto: Sistema de Gerenciamento de Alunos
# 🎯 Objetivo

# Criar um sistema em terminal para cadastrar, listar, buscar, atualizar e
# remover alunos, além de calcular médias e status (Aprovado/Reprovado).

import os

import json



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    print("[1] Cadastrar aluno")
    print("[2] Listar alunos")
    print("[3] Buscar aluno")
    print("[4] Atualizar")
    print("[5] Remover aluno")
    print("[6] Situação do aluno")
    print("[7] Sair")

def salvar_dados(alunos, arquivo='alunos.json'):
    """Salva a lista de alunos em JSON"""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)

def carregar_dados(arquivo='alunos.json'):
    """Carrega a lista de alunos de um arquivo JSON, retorna lista vazia se não existir"""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            if isinstance(dados, list):
                return dados
    except FileNotFoundError:
        pass
    return []

def cadastrar_aluno(alunos):
    limpar_tela()
    print(f"{'=== CADASTRO DE ALUNO ===':^58}")
    print(f"{'Carregue ENTER para cancelar':^58}")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome.strip():
        print('❌  Operação cancelada.')
        input('Carregue "ENTER" para continuar...')
        return
        
    if nome.isdigit():
        print('⚠️  Não pode conter números.')
        input('😀  Carregue "ENTER" para continuar...')
        return
    
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print('⚠️  Aluno já cadastrado!')
            input("Pressione ENTER para continuar...")
            return

    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    notas = [n1, n2]
    
    aluno = {'nome': nome, 'notas': notas}
    alunos.append(aluno)
    print(f"\n{nome} cadastrado com sucesso.")
    salvar_dados(alunos)
    input("\nPressione ENTER para continuar...")

def listar_alunos(alunos):
    print('=-=-' *10)
    print(f"{'=== HISTÓRICO DOS ALUNOS ===':^40}")
    print('=-=-' *10)

    for aluno in sorted(alunos, key=lambda a: a['nome'].lower()):
        print(f"Nome : {aluno['nome']}\
        \n1ª nota: {aluno['notas'][0]}\
        \n2ª nota: {aluno['notas'][1]}")
        print('=-=-' *10)
    input('Carregue "ENTER" para continuar...')
        

def remover_aluno(alunos):
    listar_alunos_por_indice(alunos)
    print(f"{'=== REMOVER ALUNO ===':^68}")
    
    try:
        codigo = int(input('Digite o código do aluno (carregue "ENTER" p/cancelar: ): '))
        indice = codigo - 1
        print(indice)
        if indice < 0 or indice >= len(alunos):
            print('⚠️  Opção inválida.')
            input("Pressione ENTER para continuar...")
            return
    except ValueError:
        print('❌ Operação cancelada.')
        input("\nPressione ENTER para continuar...")
        return
    
    aluno_removido = alunos.pop(indice)

    print(f"✅ Aluno {aluno_removido['nome']} removido com sucesso.")
    input("\nPressione ENTER para continuar...")

def buscar_aluno(alunos):
    limpar_tela()
    
    while True:
    
        nome = input("Nome do aluno (carregue 'ENTER' para cancelar: ) ").strip()
        
        if not nome.strip():
            print("❌  operação cancelada pelo usuário.")
            input('\nCarregue "ENTER" para continuar...')
            return
        
        if nome.isdigit():
            print("⚠️  Não pode conter números.")
            input('\nCarregue "ENTER" para continuar...')
            return
        
        aluno_encontrado = None
        for aluno in alunos:
            if nome.lower() == aluno['nome'].lower():
                aluno_encontrado = aluno
                break
        
        if not aluno_encontrado:
            print(f"Não temos o cadastro de {nome}")
            input('\nCarregue "ENTER" para continuar...')
            return
        
        print("=-=-" *10)
        print(f"Dados atuais do aluno encontrado: ")
        print(f"nome : {aluno['nome']}\
            \nprimeira nota: {aluno['notas'][0]}\
            \nsegunda nota: {aluno['notas'][1]}")
        print('=-=-' *10)
        input('\nCarregue "ENTER" para continuar...')
        return
    
def listar_alunos_por_indice(alunos):
    print("=-" * 34)
    print(f"{'COD'} |             {'NOME'}                 |   {'NOTAS'}")
    print("=-" * 34)

    for i, dados in enumerate(alunos, start=1):
        print(f" {i}  | {dados['nome']:<30}   |  {dados['notas'][0]:<5.1f} {dados['notas'][1]}")
    

def atualizar_dados(alunos):
    limpar_tela()
    while True:
        limpar_tela()
        print('=== ATUALIZAÇÃO DOS DADOS DOS ALUNOS ===')
        print('[1] para atualizar o nome')
        print('[2] para atualizar as notas')
        print('[3] para sair')
        
        try:
            opção = int(input('Digite o código do aluno: '))
            
            if opção < 1 or opção > 3:
                print("opção inválida.")
                input('\nCarregue "ENTER" para continuar...')
                continue
            
        except ValueError:
            print('opção inválida.')
            input('\nCarregue "ENTER" para continuar...')

        if opção == 1:
            limpar_tela()
            listar_alunos_por_indice(alunos)

            print("=-" * 30)


            try:
                codigo = int(input("Digite o código do aluno:"))
                indice = codigo - 1

                if indice < 0 or indice >= len(alunos):
                    print("Código inválido.")
            except ValueError:
                print("opçãp inválida. ")
                input('\nCarregue "ENTER" para continuar...')

            aluno = alunos[indice]
            

            print("\n=== ALUNO SELECIONADO ===")
            print(f"Nome: {aluno['nome']}")
            print(f"1ª nota: {aluno['notas'][0]}")
            print(f"2ª nota: {aluno['notas'][1]}")
            input('\nCarregue "ENTER" para continuar...')

            novo_nome = input("Digite o nome atualizado? ")
            aluno.update({'nome': novo_nome})
            print(f"✅  Nome de {novo_nome} atualizado com sucesso. ")
            salvar_dados(alunos)

            input('\nCarregue "ENTER" para continuar...')

        if opção == 2:
            while True:
                limpar_tela()
                print(f"{'=== ATUALIZAÇÃO DE NOTAS ===':^68}")
                listar_alunos_por_indice(alunos)
                print("=-" * 34)
                try:
                    codigo = int(input('\nDigite o código do aluno: '))

                    if codigo < 0 or codigo > len(alunos):
                        print("⚠️ Opção inválida.")
                    else:
                        indice = codigo - 1
                        break
                except ValueError:
                    print('⚠️  Opção inválida')
                
            while True:
                print('\n[1] para atualizar a 1º nota:')
                print('[2] para atualizar a 2º nota:')
                print('[3] para sair:')
                
                
                try:
                    escolha_nota = int(input("digite o código desejado: "))
                    if escolha_nota < 1 or escolha_nota > 3:
                        print("⚠️ Opção inválida.")
                        input('\nCarregue "ENTER" para continuar...')
                        continue
                    
                except ValueError:
                    print('  Opção inválida.')
                    continue
                if escolha_nota == 1:
                    while True:
                        try:
                            nova_nota = float(input("Digite a nota: "))
                            break
                        except ValueError:
                            print("⚠️  Nota inválida.")
                            input('\nCarregue "ENTER" para continuar...')
                            return
                
                    aluno = alunos[indice]
                    aluno['notas'][0] = nova_nota
                    print(f"a nota de {aluno['nome']} foi atualiza com sucesso.")
                    salvar_dados(alunos)
                    input('\nCarregue "ENTER" para continuar...')
                    return
                elif escolha_nota == 2:
                    while True:
                        try:
                            nova_nota = float(input("Digite a nota: "))
                            break
                        except ValueError:
                            print("⚠️  Nota inválida.")
                            input('\nCarregue "ENTER" para continuar...')
                            continue
                
                    aluno = alunos[indice]
                    aluno['notas'][1] = nova_nota
                    print(f"a nota de {aluno['nome']} foi atualiza com sucesso.")
                    salvar_dados(alunos)
                    input('\nCarregue "ENTER" para continuar...')
                    return
                else:
                    return
        else:
            return
    

def situação_aluno(alunos):
    limpar_tela()

    listar_alunos(alunos)

    nome = input('Digite o nome do aluno: ').lower()
    limpar_tela()
    total = None
    for dados in (alunos):
        if nome.lower() == dados['nome'].lower():
            total = sum(dados['notas'])
            media = total / len(dados['notas'])
            if media >= 7:
                print(f"\nNome: {dados['nome']}\nmédia: {media:.1f}\nStatus: ✅ Aprovado!")
                # input('\nCarregue "ENTER" para continuar...')
            elif media >= 5 and media < 7:
                print(f"\nNome: {dados['nome']}\nmédia: {media:.1f}")
                print("Status: ⚠️  Recuperação")
                # input('\nCarregue "ENTER" para continuar...')
            else:
                print(f"\nNome: {dados['nome']}\nMédia: {media}")
                print("Status: ❌  Reprovado!")
    if not total:
        print('Aluno não encontrado.')

    input("\nPressione ENTER para continuar...")


#       PROGRAMA PRINCIPAL
alunos = carregar_dados()

while True:
    while True:
        limpar_tela()
        menu()
        try:
            opção = int(input("Escolha sua opção desejada? "))
            if opção < 1 or opção > 7:
                print("⚠️  Opção inválida.")
                input('Carregue "ENTER" para continuar...')
            else:
                break
        except ValueError:
            print("⚠️  Opção inválida.")
            input('Carregue "ENTER" para continuar...')
            continue
        
    match opção:
        case 1:
            cadastrar_aluno(alunos)
        case 2:
            listar_alunos(alunos)
        case 3:
            buscar_aluno(alunos)
        case 4:
            atualizar_dados(alunos)
        case 5:
            remover_aluno(alunos)
        case 6:
            situação_aluno(alunos)
        case 7:
            break

print(alunos)

# [{'nome': 'João Paulo Pedrosa Soares', 'notas': [9.68, 9.85]}]

