dice_throw_history = [6, 6, 1, 2, 4, 2, 1, 5, 4, 5, 6, 6, 3, 6, 2, 6, 3, 5, 5, 6]

longest_odd_list = []
longest_odd_index = 0
to_check = []


#go thrue the list 
for i in range(0,len(dice_throw_history) - 1):
    #check if the curent integer is the same as the next 
    if dice_throw_history[i] == dice_throw_history[i+1]:
        #add to the List that will bi testet if the sequence is broken up
        to_check.append(dice_throw_history[i])
    else: 
        #to add the last interger in the seqence 
        to_check.append(dice_throw_history[i])
        #Check if the current cequence is longer and Odd
        if len(to_check) >= len(longest_odd_list) and to_check[0] % 2 == 1:
            longest_odd_list = []
            for c in to_check: longest_odd_list.append(c)
            longest_odd_index = i - len(to_check)
            to_check = []
        #reset value
        else: to_check = []
        
print(f"The longest sequence of consecutive odd numbers starts at index {longest_odd_index}, length {len(longest_odd_list)}.")



    
        
    