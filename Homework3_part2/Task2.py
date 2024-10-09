'''
Main:
    random "list" 100 items | Range(0 - > 10)

funk: "count_occurrences" (list): 
    Use dicturnary (keys 0 -> 9)

    return sorted dicturnary

Output: 
    for i in range(10): #i is the key
        Number (I + 1) occurs {i} times.

'''
import random

random_list = []

#create random list with 100 elements
for i in range(100): 
    random_list.append(random.randint(1,10))

def count_occurrences(list):
    dicturnary = {x:0 for x in range(10)}
    for e in list:
        dicturnary[e - 1] += 1
    return dicturnary

number_of_occurences = count_occurrences(random_list)

for i in range(10):
    print(f"Number {i + 1} occurs {number_of_occurences[i]}")