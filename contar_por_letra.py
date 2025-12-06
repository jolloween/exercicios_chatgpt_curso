# Crie uma função que receba uma lista de nomes e uma letra, e retorne quantos começam com essa letra.

def contar_por_letra(nomes, Letra):
    contador = 0
    for nome in nomes:
        if nome.startswith(Letra): # startswith o inicio da letra da  palavra
            contador += 1
    return contador


print("Quantidade de nomes que começam com a letra 'A': ", end="")
print(contar_por_letra(["Ana", "Alice", "Bruno", "Amanda"], "A"))
