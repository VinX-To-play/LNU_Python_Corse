import numpy as np
import random
import Visulasation as vis
import game_funktion as gf

def start_up():
    max_player = 3
    game_data_table = np.empty((max_player,21))
    game_data_table[:] = np.nan
    np.nan_to_num(game_data_table[0:,20],copy = False)
    print(game_data_table)
    return game_data_table
      

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
                vis.print_dice(dice)
                user_input = int(input("\nChous dice withe number 1 -> 6, 0 to exit"))
                if user_input > 0 and user_input <=6: rerole_dice_list.append(user_input)
                elif user_input == 0: 
                    print('rerowling')
                    break
                else:print('only Integers 0 -> 6 are valid')
            break
        except ValueError: print("only numbers valid")

        if len(rerole_dice_list) == 0:
            for i in rerole_dice_list:
                dice[i - 1] = random.randint(1,6)
            dice = sorted(dice)
            user_input = np.nan
            user_throw -= 1
        else:
            game_data_table[curent_player,20] = user_throw
            vis.print_dice(dice)
            break
    return game_data_table, dice

def user_option(dice, game_data_table, curent_player):
    number_of_options = 0
    posible_option = []
    print('Posibile option:')
    
    #if there is no option to chose    
    print('There are no compatible option, there for you need to cross one out.')
    for cell in range(20):
        if np.isnan(game_data_table[curent_player,cell]) == False: posible_option.append(cell + 1)

    for option in posible_option:
        match option:
            case 1:  print(f' 1| Ones            |{gf.upper_one(dice):^2}')
            case 2:  print(f' 2| Twos            |{gf.upper_two(dice):^2}')
            case 3:  print(f' 3| Threes          |{gf.upper_three(dice):^2}')
            case 4:  print(f' 4| Fours           |{gf.upper_four(dice):^2}')
            case 5:  print(f' 5| Fives           |{gf.upper_five(dice):^2}')
            case 6:  print(f' 6| Six             |{gf.upper_six(dice):^2}') 
            case 7:  print(f' 7| One Pair        |{gf.one_pair(dice):^2}')
            case 8:  print(f' 8| Tow Pairs       |{gf.two_pairs(dice):^2}')
            case 9:  print(f' 9| Three Pairs     |{gf.three_pairs(dice):^2}')
            case 10: print(f'10| Three of a Kind |{gf.three_of_kind(dice):^2}')
            case 11: print(f'11| Four of a Kind  |{gf.four_of_kind(dice):^2}')
            case 12: print(f'12| Five of a Kind  |{gf.five_of_kind(dice):^2}')
            case 13: print(f'13| Small straight  |{gf.small_straight(dice):^2}')
            case 14: print(f'14| Long straight   |{gf.big_straight(dice):^2}')
            case 15: print(f'15| Full straight   |{gf.full_straight(dice):^2}')
            case 16: print(f'16| Castle(Villa)   |{gf.villa(dice):^2}')
            case 17: print(f'17| Full Hous       |{gf.full_house(dice):^2}')
            case 18: print(f'18| Tower           |{gf.tower(dice):^2}')
            case 19: print(f'19| Chance          |{gf.chance(dice):^2}')
            case 20: print(f'20| Maxi-Yatzy      |{gf.maxi_yatzy(dice):^2}')

    

def main():
    game_data_table = start_up()
    while np.isnan(game_data_table).any() == True:
        break

main()
