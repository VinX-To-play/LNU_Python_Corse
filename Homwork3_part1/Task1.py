user_iterrations = 1
user_int_list = []
new_user_input = 0

print("Enter positive integers. End by giving a negative integer.")

while new_user_input >= 0:
    new_user_input = int(input(f"Integer {user_iterrations}: "))
    user_iterrations += 1
    if new_user_input >= 0 :
        user_int_list.append(new_user_input)

print(f"Number of positive integers: {user_iterrations - 2}")
print("Positive numbers:", end=" ")
for i in range(len(user_int_list)):
    print(user_int_list[i], end=", ")    