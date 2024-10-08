'''
list with 100 values
    random (1, 100)

function(difernt): random list --> list of uniqe values
    using sets
    sorting? 

print result in row with 10 elements

'''
import random
random_list = []
for i in range(100): 
    random_list.append(random.randint(1,101))
print(random_list)