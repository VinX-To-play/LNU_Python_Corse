import random

def random_values(amount, start, stop):
    output = []
    for i in range(amount):
        output.append(random.randrange(start,stop+1))
    return output

def filter_even(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0: even_numbers.append(i)
    return even_numbers
    
def sum_of_list(numbers):
    return sum(numbers)

def capitalise_names(names):
    new_names = []
    for curent_name in names:
        new_names.append(curent_name[0].upper() + curent_name[1:len(curent_name)])
    return new_names

def is_strictly_increasing(number):
    for i in range(0,len(number)-1):
        if number[i] > number[i + 1]:
            return False
    return True

def get_unique_element(number):
    unique_number = []
    for i in number:
        if i not in unique_number:
            unique_number.append(i)
    return unique_number
