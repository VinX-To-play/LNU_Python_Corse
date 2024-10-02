import random

def number_plate_nr():
    output = chr(random.randint(65, 90))
    output += chr(random.randint(65, 90))
    output += chr(random.randint(65, 90))
    output += str(random.randint(0,10))
    output += str(random.randint(0,10))
    if random.randint(0,2) == 0: output += chr(random.randint(65, 90))
    else: output += str(random.randint(0,10))
    return output
    