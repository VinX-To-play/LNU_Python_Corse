import numpy as np
from collections import Counter

lst = [3, 3, 3, 3, 3, 3]
arr = np.array(lst)

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

# Finds the number of pairs
def n_Pairs(lst):
    amount = Counter(lst)
    pairs = sum(count // 2 for count in amount.values())  # Count all pairs
    return pairs

def one_pair(lst):
    amount = Counter(lst)
    pairs = [i for i, count in amount.items() if count == 2]
    if len(pairs) == 1:
        return pairs[0]
    else:
        return None

def two_pairs(lst):
    amount = Counter(lst)
    pairs = [i for i, count in amount.items() if count == 2]
    if len(pairs) == 2:
        return pairs
    else:
        return None

def three_pairs(lst):
    amount = Counter(lst)
    pairs = [i for i, count in amount.items() if count == 2]
    if len(pairs) == 3:
        return pairs
    else:
        return None

def three_of_kind(lst):
    amount = Counter(lst)
    for num, count in amount.items():
        if count == 3:
            return num
    return None

def four_of_kind(lst):
    amount = Counter(lst)
    for num, count in amount.items():
        if count == 4:
            return num
    return None

def five_of_kind(lst):
    amount = Counter(lst)
    for num, count in amount.items():
        if count == 5:
            return num
    return None

def six_of_kind(lst): #returns not the points 
    amount = Counter(lst)
    for num, count in amount.items():
        if count == 6:
            return num
    return None

def small_straight(lst): #returns not the points
    if all(num in lst for num in range(1, 6)):
        return [1, 2, 3, 4, 5]
    else:
        return None

def big_straight(lst):
    if all(num in lst for num in range(2, 7)):
        return [2, 3, 4, 5, 6]
    else:
        return None

def full_straight(lst):
    if all(num in lst for num in range(1, 7)):
        return [1, 2, 3, 4, 5, 6]
    else:
        return None
 
    
def full_house(lst):
    pair = one_pair(lst)
    three_kind = three_of_kind(lst)
    
    if pair and three_kind:
        return pair, three_kind
    else:
        return None
    
  
def tower(lst):
    pair = one_pair(lst)
    four_kind = four_of_kind(lst)
    
    if pair and four_kind:
        return pair, four_kind
    else:
        return None

def villa(lst):
    return 0

def maxi_yatzy(lst):
    amount = Counter(lst)
    for num, count in amount.items():
        if count == 6:
            return num
    return None

print(f"Sum of ones: {upper_one(lst)}")
print(f"Sum of twos: {upper_two(lst)}")
print(f"Sum of threes: {upper_three(lst)}")
print(f"Sum of fours: {upper_four(lst)}")
print(f"Sum of fives: {upper_five(lst)}")
print(f"Sum of sixes: {upper_six(lst)}")
print(f"Number of pairs: {n_Pairs(lst)}")
print(f"One pair: {one_pair(lst)}")
print(f"Two pairs: {two_pairs(lst)}")
print(f"Three pairs: {three_pairs(lst)}")
print(f"Three of a Kind: {three_of_kind(lst)}")
print(f"Four of a Kind: {four_of_kind(lst)}")
print(f"Five of a Kind: {five_of_kind(lst)}")
print(f"Six of a Kind: {six_of_kind(lst)}")
print(f"Small Straight: {small_straight(lst)}")
print(f"big Straight: {big_straight(lst)}")
print(f"full Straight: {full_straight(lst)}")
print(f"full House: {full_house(lst)}")
print(f"tower: {tower(lst)}")
print(f"max yatzy: {maxi_yatzy(lst)}")