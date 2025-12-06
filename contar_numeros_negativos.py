# ✅ Exercício 5 — Contar números negativos

# Crie uma função que receba uma lista de números e conte quantos são negativos.

# Exemplo:

# Entrada: [-3, 2, -8, 5]
# Saída: 2

numeros = [-3, 2, -8, 5]
numeros_negativos = []

def contar_numeros_negativos():
    negativos = 0
    for n in numeros:
        if n < 0:
            negativos += 1
            numeros_negativos.append(n)
    return negativos

quantidade = contar_numeros_negativos()
print(f'lista dos números negativos: {numeros_negativos}')
print(f'quantidade de números negativos: {quantidade}')
