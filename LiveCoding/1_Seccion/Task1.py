needs_to_loop = True
even = 0
odd = 0

while needs_to_loop == True:
    user_int = int(input("Enter a number (0 to stop): "))
    
    if user_int == 0: needs_to_loop = False
    elif user_int % 2 ==0: even += 1
    else: odd += 1
    
print("The number of odd:", odd)
print("The number of even", even)
    