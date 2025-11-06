# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print("Pergunta: ",perguntas[0]['Pergunta'])
print('opções:')

acertos = 0
errou = 0
    
for indices, opcoes in enumerate(perguntas[0]['Opções']):
    print(indices,")", opcoes)

while True:
    
    try:
        escolha = int(input('Escolha uma opção: '))
        if perguntas[0]['Opções'][escolha] == perguntas[0]['Resposta']:
            acertos += 1
            print("acertou 👍")
        else:
            errou += 1
            print("😯 errou")
        break
    
        
    except ValueError:
        print("❌ digite uma opção válida")
print("-=" *20)
print("Pergunta: ",perguntas[1]['Pergunta'])
print('opções:')

for indices, opcoes in enumerate(perguntas[1]['Opções']):
    print(indices,")", opcoes)

while True:
    
    try:
        escolha = int(input('Escolha uma opção: '))
        if perguntas[1]['Opções'][escolha] == perguntas[1]['Resposta']:
            acertos += 1
            print("acertou 👍")
        else:
            errou +=1
            print("😯 errou")
        break
    
        
    except ValueError:
        print("❌ digite uma opção válida")

print("-=" *20)
print("Pergunta: ",perguntas[2]['Pergunta'])
print('opções:')

for indices, opcoes in enumerate(perguntas[2]['Opções']):
    print(indices,")", opcoes)

while True:
    
    try:
        escolha = int(input('Escolha uma opção: '))
        if perguntas[2]['Opções'][escolha] == perguntas[2]['Resposta']:
            acertos +=1
            print("acertou 👍")
        else:
            errou += 1
            print("😯 errou")
        break
    
        
    except ValueError:
        print("❌ digite uma opção válida")
            
if acertos > 0:
    print("-=" *20)
    print(f"acertou {acertos}/3 das perguntas")
    porcentagem = (acertos / 3) * 100
    print(f"Aproveitamento de {porcentagem:.2f}%")
else:
    print("-=" *20)
    print("⚠️  Errou todas as questões\nboa sorte na próxima vez!")



