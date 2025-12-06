# ✅ Exercício 9 — Converter temperaturas Fahrenheit → Celsius

# Crie uma função que receba uma lista de temperaturas em Fahrenheit
#  e retorne uma lista com todas convertidas para Celsius usando:

# C = (F - 32) * 5/9
# Exemplo:
# Entrada: [32, 50, 77]
# Saída: [0, 10, 25]
fahrenheit = [32, 50, 77] # fahrenheit
celsius = []

def conversor_temperatura():
    for F in fahrenheit:
        c = (F - 32) * 5 / 9
        celsius.append(int(c))

conversor_temperatura()
print(f'Lista em Fahrenheit: {fahrenheit}')
print(f'Minha lista convertida em celsius: {celsius}')





