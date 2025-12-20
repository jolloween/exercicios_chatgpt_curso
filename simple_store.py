# 3. Loja Simples

# Produtos {nome: preço}

# Função para alterar preço.

# - A função deve:

# - Receber o dicionário de produtos

# - Receber o nome do produto

# - Receber o novo preço

# - Alterar o preço se o produto existir

# - Avisar se o produto não existir

# Informar produtos acima de determinado valor.

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

produtos = {
        'arroz': 1.30,
        'feijão': 1.19,
        'café': 4.99,
        'sorvete': 2.79,
        'macarrão': 0.89,
        'cerveja': 1.79,
        'manteiga': 2.39,
        'colgate': 1.79,
        'leite': 0.89
}

def alterar_preco(produtos, produto):
    if produto not in produtos:
        print(f"Não temos {produto} no estoque.")
        while True:
            resp = input(f"Quer adicionar {produto} ao estoque? [S/N] ").upper()
            if resp == 'S':
                try:
                    preco = float(input(f"Qual o preço do(a) {produto}? $"))
                    produtos[produto] = preco
                    print(f"produto '{produto}' adicionado com sucesso.")
                    break
                except ValueError:
                    print("⚠️  Digite um preço válido.")
            else:
                break
    else:
        while True:
            resp = input("desejas alterar o preço? [S/N] ").upper()
            if resp == "S":
                novo_preco = float(input(f"Digite o novo valor do produto '{produto}'"
                                        f" Preço: ${produtos[produto]:.2f}? "))
                produtos[produto] = novo_preco
                print(f"'{produto}' teve o preço alterado para ${novo_preco:.2f}")
                break
            else:
                break
    

limpar_tela()
while True:
    produto = input("Digite o nome do produto para adicionar ou alterar o preço: ")
    alterar_preco(produtos, produto)
    while True:
        resp = input("Quer continuar: [S/N] ").upper()
        if resp not in ('S', 'N'):
            print("⚠️  Digite 'S' para sim e 'N' para não.")
        else:
            break
    if resp == 'N':
        break

limpar_tela()
print("=-" *20)
print(">>> PRODUTOS DO ESTOQUE ATUALIZADO <<<")
print("=-" *20)
for nome, valor in produtos.items():
    print(f"Produto: {nome.title():<10} {'|':<5} Preço: ${valor:.2f}")

# Mostrar produtos acima de determinado valor

print("")
print("=-" *20)
valor_ref = float(input("Mostrar produtos acima de qual valor? $"))
print("=-" *20)
print(f"Produtos com preço acima de ${valor_ref:.2f}:")
print("=-" *20)
for nome, preco in produtos.items():
    if preco > valor_ref:
        print(f"Produto: {nome.title():<10} {'|':<5} Preço: ${preco:.2f}")
    

