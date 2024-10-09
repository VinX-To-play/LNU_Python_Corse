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

#create random list with 100 elements
for i in range(100): 
    random_list.append(random.randint(1,100))

def diferent(random_list):
    first = True
    uniqe_random_list = []
    #make a set out of a list
    set_from_random_list = set(random_list)
    #convert back to a list
    for x in set_from_random_list:
        #check if first time becouse 1. value reaturns the biggest value
        if first == True:
            cash = x
            first = False
        #add rest frome smalest to next biggst
        uniqe_random_list.append(x)
    #adds bigest to the end
    uniqe_random_list.append(cash)
    return uniqe_random_list

random_list = diferent(random_list)
#print output
print(f"Number of unique integers: {len(random_list)}")
print("Diferent integer:")

for e in range(len(random_list)):
    #check if thear are 10 elementis in the row
    if e % 10 == 0 and e != 0 : print()
    #print current element
    print(f"{random_list[e-1]:>3}",end=" ") 