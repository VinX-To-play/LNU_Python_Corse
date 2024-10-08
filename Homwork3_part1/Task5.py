#set up Vars
running = True

#Funktion to test if a string is a palindrome
def is_palindrome(to_test_str):
    #set up variabel
    to_test_str_reverst = ""
    stript_to_test = ""
    #set string to only lowercas and strip blankspace
    to_test_str = to_test_str.lower()
    for i in to_test_str:
        if i.isalpha() == True: stript_to_test += i
    #reverse string 
    for i in range(len(stript_to_test),0,-1):
        to_test_str_reverst += stript_to_test[i -1]
    #return it it is or isn't a palindrome
    return to_test_str_reverst == stript_to_test


#main program loop
while running == True:
    #get User string
    user_string = input("Enter a String: ")
    if user_string != "stop":
        #test if it is a palindrom
        palindrome = is_palindrome(user_string)
        #check if there is a need to add a "not" to the string
        if palindrome == True: palindrome_str = ""
        else: palindrome_str = "not "
        #print the result
        print(f"This is {palindrome_str}a palindrom")
    else: break
  
print("Program will end now")