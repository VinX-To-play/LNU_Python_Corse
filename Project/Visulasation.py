import numpy as np

def draw_table(table):
    print()
    for r in range(np.shape(table)[0]):
        print(f'Player {r:^2} | Ones: {table[r,0]:^2} | Tows: {table[r,1]:^2} | Three: {table[r,2]:^2} | Fore: {table[r,3]:^2} | Five: {table[r,4]:^2} | Six: {table[r,5]:^2} | One Pair: {table[r,6]:^2} | Tow Pairs: {table[r,7]:^2} | Three Pairs: {table[r,8]:^2} | 3 of a kind: {table[r,9]:^2} | 4 of a kind: {table[r,10]:^2} | 5 of a kind: {table[r,11]:^2} | Smal straight: {table[r,12]:^2} | Large Straight: {table[r,13]:^2} | Full Straight : {table[r,14]:^2} | Castle(Villa): {table[r,15]:^2} | Full hous: {table[r,16]:^2} | Tower: {table[r,17]:^2} | Chance: {table[r,18]:^2} | Maxi Yatzy: {table[r,19 ]:^3}')

def print_dice(dice):
    print()
    print('Dice number:',end='')
    for e in range(1,7) :
        print(f'{e:^4}|',end='')
    print('\n','-' * 40)
    print('Dice value: ',end='')
    for e in dice:
        print(f'{e:^4}|',end='')

def end_score(table, max_player):
    for player in range(max_player):
        print(f'End score Player {player + 1} : {sum(table[player,:])}')

def highscore(table):
    print('Highscore:')
    if table.shape[0] < 10: length_to_show = table.shape[0]
    else: length_to_show = 10
    for i in range(length_to_show):
        print(f'{(i + 1):^2} | {table[i, 0]:^3} Points | {table[i, 1]}')