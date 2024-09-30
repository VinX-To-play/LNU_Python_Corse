user_int = int(input("Give an integer:"))

if user_int < 0: 
    print("Input a positiv interger!")
    exit()

to_test = 0
total_zeros = 0
total_odd = 0
total_even = 0

while user_int > 0:
    to_test = user_int % 10 #get the lowest digit (because working in base 10)
    if to_test % 2 != 0: total_odd += 1
    elif to_test == 0: total_zeros +=1
    else: total_even +=1
    user_int = user_int // 10 #remove lowest digit 
    
print("Zeros:",total_zeros)
print("Even:",total_even)
print("Odd:",total_odd)
    
    