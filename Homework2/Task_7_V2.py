#set up variobels
program_run = True

#Menu
def Menu():
    menu_str = """Select a calculation:
    1. Slope of a line
    2. Midpoint of two points
    3. Area of a triangle
    0. Exit"""
    print(menu_str)
    user_choice = int(input("Enter your choice (0-3): "))

    #Input checks
    if user_choice < 0 or user_choice > 3: print("\nOnly input betwin 0-3 is exepted! ¯\_(ツ)_/¯")   

    #check if nececery ot get point info
    if user_choice == 0:
        print("Thanks for runing. (ಠ‿‿ಠ)")
        program_run = False
    
        

def input(user_choice):
    #get nececery point info
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    if user_choice == 3:
        x3 = int(input("Enter x3:"))
        y3 = int(input("Enter y3:"))

#Clculating functions
#slope of a line funktion
def slope(x1, y1, x2, y2):
    output = ((y2 - y1) / (x2 -x1))
    return output

#midpoint betwin two points
def midpoint(x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return midpoint_x, midpoint_y

#area of a triangle
def trangle_area(x1, y1, x2, y2, x3, y3):
    output = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) * 0.5
    return output



#Program loop
while program_run == True:
    Menu()
    input()
    #Program exits
    if user_choice == 1:
        print(f"The slope of the line through ({x1:.1f}, {y1:.1f}) and ({x2:.1f}, {y2:.1f}) is {slope(x1, y1, x2, y2):.1f}.")
    elif user_choice == 2:
        print(f"The midpoint between ({x1:.1f}, {y1:.1f}) and ({x2:.1f}, {y2:.1f}) is ({midpoint(x1, y1, x2, y2)[0]:.1f}, {midpoint(x1, y1, x2, y2)[1]:.1f})")
    elif user_choice == 3:
        print(f"The area of the triangle with vertices ({x1:.1f}, {y1:.1f}), ({x2:.1f}, {y2:.1f}), ({x3:.1f}, {y3:.1f}) is {trangle_area(x1, y1, x2, y2, x3, y3):.1f}.")
    else:print("IDK how you got hear! ¯\_(ツ)_/¯")

