nr_iterrations = int(input("enter a positive integer:"))

if nr_iterrations < 1:
    print("Pleas only input positiv Numbers.")
    
else:
    print("Odd numbers using for:", end=" ")
    for i in range(1,nr_iterrations,2):
            print(i ,end=" ")
    
    print()
    
    i = 1
    print("Odd numbers using while:", end=" ")
    while i < nr_iterrations:
        print(i ,end=" ")
        i = i + 2
            
