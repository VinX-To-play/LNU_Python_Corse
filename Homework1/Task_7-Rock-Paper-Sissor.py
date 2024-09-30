import random

com_chois = random.randint(0,2)

print('Enter your choice:')
print('0 for scissors, 1 for rock, 2 for paper')
player_chois = int(input('>>>'))

def convert_game_object (num):
    if (num == 0) :
        object_name = 'scissors'
    
    elif (num == 1): 
        object_name = 'rock'
        
    elif (num == 2):
        object_name = 'paper'
    
    return object_name
        
    
def game_winner (computer , player):
    if (computer == player):
        return 'Its a draw'
    
    elif (computer == 0):
        if (player == 1):
            return 'You Win!'
        else: return 'You lose!'
        
    elif (computer == 1):
        if (player == 2):
            return 'You Win!'
        else: return 'You lose!' 
        
    elif (computer == 2):
        if (player == 0):
            return 'You Win!'
        else: return 'You lose!' 

print('Your choice:', convert_game_object (player_chois))
print("Computer's choice:", convert_game_object(com_chois))
print(game_winner(com_chois, player_chois))

