triangle_base = int(input("Enter an odd positive integer:"))
if triangle_base < 0 or triangle_base % 2 == 0:
    print("input positiv odd interger!")
else:
    print("Right-Angled Triangle")
    for i in range(triangle_base,0,-1):
        print(" " * (triangle_base - i), end="")
        print("*" * i)

    print("Isosceles Triangle:")
    for i in range (1,triangle_base+1,2):
        blank_space = (triangle_base - i) // 2
        print(" " * blank_space, end="")
        print("*" * i)
    