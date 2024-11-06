from collections import Counter
# Spoke with Daniel wich is why we looked in to the libary. 
# Counter class is a special type of object data-set provided with the collections module in Python3
# reference from https://www.geeksforgeeks.org/python-counter-objects-elements/
# A Counter is a subclass of dict. Therefore it is an unordered collection where elements and their respective count are stored as a dictionary. This is equivalent to a bag or multiset of other languages.
# reference for max-yatzy points https://www.holdson.com/images/uploaded/MaxiYatzy_rules_UK.pdf


def upper_one(lst):
    sum_ones = 0
    for i in lst:
        if i == 1:
            sum_ones += 1
    return sum_ones

def upper_two(lst):
    sum_twos = 0
    for i in lst:
        if i == 2:
            sum_twos += 2
    return sum_twos

def upper_three(lst):
    sum_threes = 0
    for i in lst:
        if i == 3:
            sum_threes += 3
    return sum_threes

def upper_four(lst):
    sum_fours = 0
    for i in lst:
        if i == 4:
            sum_fours += 4
    return sum_fours

def upper_five(lst):
    sum_fives = 0
    for i in lst:
        if i == 5:
            sum_fives += 5
    return sum_fives

def upper_six(lst):
    sum_sixes = 0
    for i in lst:
        if i == 6:
            sum_sixes += 6
    return sum_sixes

def one_pair(lst):
    # creats a dictunary where the key is the number on the dice and the value is the amount of acurences 
    amount = Counter(lst)
    # creats a list where each objekt is only containd tow times
    pairs = [i for i, count in amount.items() if count == 2] 
    if len(pairs) == 1:
        return sum(pairs) * 2
    else:
        return 0


def two_pairs(lst):
    amount = Counter(lst)
    pairs = [i for i, count in amount.items() if count == 2]
    if len(pairs) == 2:
        return sum(pairs) * 2
    else:
        return 0

def three_pairs(lst):
    amount = Counter(lst)
    pairs = [i for i, count in amount.items() if count == 2]
    if len(pairs) == 3:
        return sum(pairs) * 2
    else:
        return 0

def three_of_kind(lst):
    lst = lst[::-1]
    amount = Counter(lst)
    for num, count in amount.items(): # num = key | count is the item
        if count == 3:
            return num * 3
    return 0


def four_of_kind(lst):
    amount = Counter(lst)
    for num, count in amount.items(): # num = key | count is the item
        if count == 4:
            return num * 4
    return 0

def five_of_kind(lst):
    amount = Counter(lst)
    for num, count in amount.items(): # num = key | count is the item
        if count == 5:
            return num * 5
    return 0

def small_straight(lst): 
    if all(num in lst for num in range(1, 6)):
        return 15
    else:
        return 0

def big_straight(lst):
    if all(num in lst for num in range(2, 7)):
        return 20
    else:
        return 0

def full_straight(lst):
    if all(num in lst for num in range(1, 7)):
        return 21
    else:
        return 0
 
    
def full_house(lst):
    pair = one_pair(lst)
    three_kind = three_of_kind(lst)
    
    if pair and three_kind:
        return pair + three_kind
    else:
        return 0
    
  
def tower(lst):
    pair = one_pair(lst)
    four_kind = four_of_kind(lst)
    
    if pair and four_kind:
        return pair + four_kind
    else:
        return 0

def villa(lst):
    if lst[0] == lst[1] == lst[2]:
        if lst[3] == lst[4] == lst[5]:
            return sum(lst)
    return 0

def chance(lst):
    return sum(lst)

def maxi_yatzy(lst):
    amount = Counter(lst)
    for num, count in amount.items():
        if count == 6:
            return num * 6
    return 0
