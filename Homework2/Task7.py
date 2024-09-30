#set up variobels
program_run = True

def Menu():
    menu_str = """Select a calculation:
    1. Slope of a line
    2. Midpoint of two points
    3. Area of a triangle
    0. Exit"""
    print(menu_str)
    user_choice = int(input("Enter your choice (0-3): "))
    return user_choice

#Clculating functions
#slope of a line funktion
def slope(x1, y1, x2, y2):
    calcolation = ((y2 - y1) / (x2 -x1))
    output = f"The slope of the line through ({x1:.1f}, {y1:.1f}) and ({x2:.1f}, {y2:.1f}) is {calcolation:.1f}."
    return output

def midpoint(x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    output = f"The midpoint between ({x1:.1f}, {y1:.1f}) and ({x2:.1f}, {y2:.1f}) is ({midpoint_x:.1f}, {midpoint_y:.1f})"
    return output

def trangle_area(x1, y1, x2, y2, x3, y3):
    calculation = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) * 0.5
    output = f"The area of the triangle with vertices ({x1:.1f}, {y1:.1f}), ({x2:.1f}, {y2:.1f}), ({x3:.1f}, {y3:.1f}) is {calculation:.1f}"
    return output

while program_run == True:
    user_choice = Menu()
    
    if user_choice == 0: 
        print("Thanks for runing. (ಠ‿‿ಠ)")
        program_run = False
    elif user_choice < 0 or user_choice > 3:
        print("\nIDK how you got hear!\nprobebly user error with input.\nIf input was corect contect your sysadmnin  ¯\_(ツ)_/¯")  
    else:
        #get nececery point info
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        if user_choice == 3:
            x3 = int(input("Enter x3:"))
            y3 = int(input("Enter y3:"))

        #working calcolating & outputing nacecary calcolations
        if user_choice == 1: print(slope(x1, y1, x2, y2))
        elif user_choice == 2: print(midpoint(x1, y1, x2, y2))
        elif user_choice == 3: print(trangle_area(x1, y1, x2, y2, x3, y3))
    
    print()