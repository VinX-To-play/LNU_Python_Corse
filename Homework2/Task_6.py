user_number = int(input("Enter a positive interger:"))

if user_number < 0 :
    print("Please input a positiv Interger")
    exit()

def sum_of_digits(input):
    sum_of_input = 0
    while input > 0:
        sum_of_input += input % 10
        input = input // 10
    return sum_of_input

print("The sum of the number is:", sum_of_digits(user_number))
        
        
        