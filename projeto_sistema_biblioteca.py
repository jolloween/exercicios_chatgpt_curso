# 1. Sistema de Biblioteca

# Cadastrar livros (título, autor, ano, status: disponível/emprestado)

# Listar livros

# Buscar livro por título ou autor

# Emprestar/devolver livro

# Remover livro

# Salvar dados em JSON

# Aprende a trabalhar com dicionários aninhados e arquivos JSON.

import os
import time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_livros(livros):
    
    while True:
        limpar_tela()
        while True:
            cadastrar_titulo = input("Digite o Título do livro: ").strip()
            if cadastrar_titulo == "":
                print("Não pode conter espaços.")
                continue
            else:
                break
        if cadastrar_titulo in livros:
            print(f"⚠️  {cadastrar_titulo} já consta no catálogo.")
        else:
            livros[cadastrar_titulo] = {}
        
            while True:
                autor = input("Digite o autor: ").strip()
                if autor.isdigit():
                    print("⚠️  Nome do autor inválido.")
                    continue
                elif autor == "":
                    print("Não pode conter espaços.")
                    continue
                else:
                    break
            while True:
                try:
                    ano = int(input("ano: "))
                    
                    if ano < 1000 or ano >10000:
                        print("⚠️  O ano deve conter 4 números.")
                        continue
                    else:
                        break
                except ValueError:
                    print("Digite um ano válido")
                    continue
            
            #códigos para validas o cadastro
            status = 'disponível'
            dados = {'autor': autor, 'ano': ano, 'status': status }
            livros[cadastrar_titulo] = dados
            print(f"Título: {cadastrar_titulo} cadastrado com sucesso!")
            input("\nCarregue enter para continuar...")
            limpar_tela()
            #cadastrar outro livro caso o usuário queira
            resp = input("Gostaria de cadastrar outro Título? [S/N] ").upper()
            if resp == 'N':
                break

def Buscar_Livro_Autor_Titulo(livros): #buscar livro pelo autor ou título
    limpar_tela()
    while True:
        busca = input("Digite nome do autor ou título: ").lower()
        
        encontrou = False #Flag para quandf or verdadeiro o loop parar.
        print("---"*13)
        for k, v in livros.items():
            if busca == k.lower() or busca == v['autor'].lower():
                print(f"Título: {k:<60}")
                print(f"Autor: {v['autor']}")
                print(f"Ano: {v['ano']}")
                print(f"Status: {v['status']}")
                print("---"*13)
                encontrou = True
        if not encontrou:
            print(f"❌  {busca} não disponível")
            encontrou = False
        resp = input("Quer continuar a pesquisa? [S/N] ").upper()
        if resp == 'N':
            break
    # input("\nCarregue enter para continuar...")

def listar_livros(livros):
    limpar_tela()
    for k, v in sorted(livros.items()):#, key=lambda item: item[1]['autor'].lower()):
        print("---"*13)
        print(f"Título: {k:<60}")
        print(f"Autor: {v['autor']}")
        print(f"Ano: {v['ano']}")
        print(f"Status: {v['status']}")
        
    print("---"*13)
    input("\nCarregue enter para continuar...")

def emprestar_devolver_livro(livros):
    limpar_tela()
    print("MENU DE EMPRÉSTIMO E DEVOLUÇÃO")
    print("[1] Emprestar livro")
    print("[2] Devolver livro")
    print("[3] sair")
    while True:
        try:
            opção = int(input("Digite a sua opção desejada: "))
            if opção < 1 or opção > 3:
                print(print("Digite uma opção válida."))
                continue
            else: 
                break
        except ValueError:
            print("Digite uma opção válida.")


    match opção:
        case 1:
            while True:
                emprestar_livro = input("Digite o título do livro ou 'ENTER' para cancelar): ").strip()
                if emprestar_livro == "":
                    break

                pesquisa = emprestar_livro.lower()
                titulo_real = None
                
                for titulo in livros:
                    if pesquisa == titulo.lower():
                        titulo_real = titulo
                        break

                if not titulo_real:
                    print("❌  Não temos este livro em nossa biblioteca")
                    continue

                if livros[titulo_real]['status'] == 'disponível':
                    livros[titulo_real]['status'] = 'emprestado'
                    print(f"📚 {titulo_real} emprestado com sucesso!")
                else:
                    print("⚠️  O livro já está emprestado.")

                resp = input("\nQuer alugar outro livro? [S/N]: ").upper()
                if resp != "S":
                    break
            

        case 2:
            devolver_livro = input("Digite o nome do livro: ")
            if devolver_livro in livros:
                if livros[devolver_livro]['status'] == 'emprestado':
                    livros[devolver_livro]['status'] ='disponível'
                    print(f"{devolver_livro} devolvido com sucesso!")
                else:
                    print("O livro se encontra dísponivel")
            else:
                print("❌  Não temos este livro em nossa biblioteca")

        case 3:
            return
    input("\nCarregue enter para continuar...")


def remover_livro(livros):
    while True:
        remover_livro = input("Qual titulo deseja excluir ou 'ENTER para sair'? ").strip()
        if remover_livro == "":
            break
        if remover_livro in livros:
            del livros[remover_livro]
            print(f"{remover_livro} excluído com sucesso.")
        if remover_livro not in livros:
            print(f"{remover_livro} não consta este livro na biblioteca.")
        
        resp = input("Quer continuar? [S/N]").upper()
        if resp != 'S':
            break
        
    # input("\nCarregue enter para continuar...")

def menu():
    print("-"*36)
    print(f"{'MENU':^34}")
    print("-"*36)
    print("[1] cadastrar livro")
    print("[2] Listar livros")
    print("[3] Buscar livro por título ou autor")
    print("[4] Emprestar/devolver livro")
    print("[5] Remover livro")
    print("[6] sair")

limpar_tela()

livros = {
    "O Pequeno Príncipe": {
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1943,
        "status": "disponível"
    },
    "1984": {
        "autor": "George Orwell",
        "ano": 1949,
        "status": "emprestado"
    },
    "Dom Casmurro": {
        "autor": "Machado de Assis",
        "ano": 1899,
        "status": "disponível"
    },
    "Harry Potter e a Pedra Filosofal": {
        "autor": "J.K. Rowling",
        "ano": 1997,
        "status": "disponível"
    },
    "O Senhor dos Anéis": {
        "autor": "J.R.R. Tolkien",
        "ano": 1954,
        "status": "emprestado"
    },
    "A Menina que Roubava Livros": {
        "autor": "Markus Zusak",
        "ano": 2005,
        "status": "disponível"
    },
    "O Alquimista": {
        "autor": "Paulo Coelho",
        "ano": 1988,
        "status": "emprestado"
    },
    "Cem Anos de Solidão": {
        "autor": "Gabriel García Márquez",
        "ano": 1967,
        "status": "disponível"
    },
    "A Revolução dos Bichos": {
        "autor": "George Orwell",
        "ano": 1945,
        "status": "disponível"
    },
    "Memórias Póstumas de Brás Cubas": {
        "autor": "Machado de Assis",
        "ano": 1881,
        "status": "emprestado"
    }
}

while True:
    limpar_tela()
    menu() #menu da biblioteca
    
    while True:
        try:
            opção = int(input("Digite o código desejado: "))
            if opção < 1 or opção > 6:
                print("⚠️  Digite uma opção válida")
                continue
            else:
                break
        except ValueError:
            print("⚠️  Digite uma opção válida.")
            continue

    match opção:
        case 1:
            cadastrar_livros(livros)
        case 2:
            listar_livros(livros)
        case 3:
            Buscar_Livro_Autor_Titulo(livros)
        case 4:
            emprestar_devolver_livro(livros)
        case 5:
            remover_livro(livros)
        case 6:
            for i in range(3,0,-1):
                print(f"{i}",end="...")
                time.sleep(1)
            print("Fim.")
            print("❌  Programa encerrado com sucesso!")
            break


