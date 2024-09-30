import random

for x in range(1000):
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    num3 = random.randint(-100,100)

    pos1 = None
    pos2 = None
    pos3 = None

    def test_priority(high, mid, low):
        if high >= mid and mid >= low:
            return True
    
        else: return False
    
    if test_priority(num1, num2, num3): 
            pos1 = num1
            pos2 = num2
            pos3 = num3
    
    elif test_priority(num1, num3, num2):
        pos1 = num1
        pos2 = num3
        pos3 = num2
    
    elif test_priority(num2,num1,num3):
        pos1 = num2
        pos2 = num1
        pos3 = num3
    
    elif test_priority(num2,num3,num1):
        pos1 = num2
        pos2 = num3
        pos3 = num1
    
    elif test_priority(num3,num1,num2):
        pos1 = num3
        pos2 = num1
        pos3 = num2
    
    elif test_priority(num3, num2, num1):
        pos1 = num3
        pos2 = num2
        pos3 = num1
    
    if pos1 == None or pos2 == None or pos3 == None:
        print(pos1, pos2,pos3, '|', num1,num2,num3)

    