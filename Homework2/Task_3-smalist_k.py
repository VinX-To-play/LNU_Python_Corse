number = int(input("Enter a positive integer: "))

if number < 0:
    print("Please only input positv intergers!")
else:
    sum_k = 0
    k = 1
    while sum_k < number :
        sum_k += k
        k += 2
        
    print(f"{k:^2} is the smallest k such that 1+3+5+...+k > {number}")
    
    
    sum_k = 0
    k = 0
    while sum_k < number : # over shot by one 
        sum_k += k
        k += 2
    #correct over shot by a factor of 2
    # because loop 1* to menny & in loop add k to sum_k and k + 2 
    sum_k -= 2 * k
    k -= 4
    
    print(f"{k:^2} is the largest k such that 0+2+4+6+...+k < {number}")