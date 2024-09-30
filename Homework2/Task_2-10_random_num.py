import random

sum_of_odd_numbers = 0

print("All numbers: ", end="")
for i in range(10):
    my_random = random.randint(1,10)
    print(my_random, end=" ")
    if my_random % 2 != 0:
        sum_of_odd_numbers += my_random
    
print(f"\nSum of the odd numbers is: {sum_of_odd_numbers}")