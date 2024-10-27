import numpy as np
import random
max_player = 3

game_data_table = np.empty((max_player,21))
game_data_table[:] = np.nan
np.nan_to_num(game_data_table[0:,20],copy = False)
print(game_data_table)

def print_dice(dice):
    print()
    print('Dice number:',end='')
    for e in range(1,7) :
        print(f'{e:^4}|',end='')
    print('\n','-' * 40)
    print('Dice value: ',end='')
    for e in dice:
        print(f'{e:^4}|',end='')        

def dice_throw(game_data_table, curent_player):
    user_input = np.nan                                #reset user input 
    user_throw = 3 + game_data_table[curent_player,20] #set max rethrows
    dice = [random.randint(1,6) for _ in range(6)]     #rowl dice
    dice = sorted(dice)                                
    
    while user_throw != 0:  #
        rerole_dice_list = []
        try:
            while user_input != 0:
                print(f'Please select the Dice you want to rethrow (Rethrows left: {user_throw}): ')
                print_dice(dice)
                user_input = int(input("\nChous dice withe number 1 -> 6, 0 to exit"))
                if user_input > 0 and user_input <=6: rerole_dice_list.append(user_input)
                elif user_input == 0: 
                    print('rerowling')
                else:print('only Integers 0 -> 6 are valid')
            exit
        except ValueError: print("only numbers valid")

        if len(rerole_dice_list) == 0:
            for i in rerole_dice_list:
                dice[i - 1] = random.randint(1,6)
            dice = sorted(dice)
            user_input = np.nan
            user_throw -= 1
        else:
            game_data_table[curent_player,20] = user_throw
            break




dice_throw(game_data_table, 0)
'''
for _ in range(20 * max_player):
    dice_throw()
'''

