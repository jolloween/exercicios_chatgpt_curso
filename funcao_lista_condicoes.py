# Crie uma função que receba uma lista de números e retorne apenas os números pares.

# Exemplo:

# Entrada:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Saída esperada:
# [2, 4, 6, 8, 10]



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

def filtrar_numeros_pares():
    for n in numeros:
        # print(n)
        if n % 2 == 0:
            numeros_pares.append(n)

#programa principal
filtrar_numeros_pares()
print(numeros_pares)


