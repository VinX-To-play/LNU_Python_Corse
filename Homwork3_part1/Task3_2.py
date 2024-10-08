import random

longest_odd_list = []
longest_odd_index = 0
to_check = []
dice_throw_history = []

for _ in range(20):
    dice_throw_history.append(random.randint(1,6))

#go thrue the list 
for i in range(0,len(dice_throw_history) - 1):
    #check if current and next are Odd
    if dice_throw_history[i] % 2 != 0 and dice_throw_history[i+1] % 2 != 0:
        #add the current to the to_check list
        to_check.append(dice_throw_history[i])    
    else:
        #add the current if the current is odd
        if dice_throw_history[i] % 2 != 0: to_check.append(dice_throw_history[i])
        #check if the current seqence of odd is longer then the privies seqence
        if len(to_check) >= len(longest_odd_list):
            longest_odd_list = []
            for m in to_check: longest_odd_list.append(m)
            #set the index of the longest odd seqence in the dice_throw_history
            longest_odd_index = (i - len(to_check)) + 1
            to_check = []
        else: to_check = []
        
print("Dice rolls:", dice_throw_history)
print(f"The longest sequence of consecutive odd numbers starts at index {longest_odd_index}, length {len(longest_odd_list)}.")



    
        
    