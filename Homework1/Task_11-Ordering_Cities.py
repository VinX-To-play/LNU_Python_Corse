city1 = input('Enter the name of the first city:')
city2 = input('Enter the name of the second city:')
city3 = input('Enter the name of the third city')

num1 = ord(city1[0])
num2 = ord(city2[0])
num3 = ord(city3[0])

pos1 = None
pos2 = None
pos3 = None

def test_priority(high, mid, low):
    if high >= mid and mid >= low:
        return True
    
    else: return False
    
if test_priority(num1, num2, num3): 
    pos1 = city1
    pos2 = city2
    pos3 = city3
    
elif test_priority(num1, num3, num2):
    pos1 = city1
    pos2 = city3
    pos3 = city2
    
elif test_priority(num2,num1,num3):
    pos1 = city2
    pos2 = city1
    pos3 = city3
    
elif test_priority(num2,num3,num1):
    pos1 = city2
    pos2 = city3
    pos3 = city1
    
elif test_priority(num3,num1,num2):
    pos1 = city3
    pos2 = city1
    pos3 = city2
    
elif test_priority(num3, num2, num1):
    pos1 = city3
    pos2 = city2
    pos3 = city1
    
print('The cities in alphabetical order are:' , pos3 ,',', pos2, ',', pos1 )
