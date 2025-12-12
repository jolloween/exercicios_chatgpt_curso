# <!-- 8. Ranking de Pontuações

# Faça um programa que:

# Tenha um dicionário com nome de jogadores e suas pontuações.

# Use uma função para atualizar a pontuação de um jogador.

# Use condições para verificar se o jogador existe; se não existir, cadastre-o.

# Use um loop para permitir várias atualizações.

# Ao final, mostre o ranking do maior para o menor. -->




scores = {
    "Alice": 120,
    "Bob": 85,
    "Carlos": 200,
    "Diana": 150
}

def update_scores(player, scores):
    if player not in scores:
        print(f'{player} is not on the list.')
        while True:
            try:
                novo_score = int(input(f"What is {player}'s score? ?"))
                scores[player] = novo_score
                return
            except ValueError:
                print("Type just numbers.")
    else:
        while True:
            try:
                score = int(input(f"Enter the new score for {player}: "))
                scores[player] = score
                break
            except ValueError:
                print("Please enter a valid number.")
        
    
# Main loop for multi-player update
while True:
    
    player = input("Which player's score do you want to edit or (type 'E' to exit)? ").title()
    if player.isdigit() or player == '':
        print("Please type a valid name, not numbers.")
        continue
    if player == 'E':
        break
    update_scores(player, scores)

    # Asks if the user wants to continue.
    while True:
        choice = input("Do you want to continue? [Y] for yes or [N] for no: ").upper()
                
        if choice in ('Y', 'N'):
            break
        
        else:
            print('Type "Y" for yes and "N" for no.')
            
    if choice == 'N':
        break
#Sort the dictionary by score from highest to lowest.
sorted_score = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
# Shows the final ranking
for k, v in sorted_score.items():
    print('=-' * 20)
    print(f'Name: {k}')
    print(f'Score: {v}')
print('=-' * 20)

