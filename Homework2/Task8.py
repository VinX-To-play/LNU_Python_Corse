user_string = input("Enter a sentence:")

def reverse_words(text):
    sentince = ""
    word = ""
    
    for i in range(len(text), 0, -1):
       c = text[i-1]
       if c != " ": word += c
       elif c == " ": 
            output = ""
            for i2 in range(len(word), 0, -1): output += word[i2-1]       
            sentince += output
            sentince += " "
            word = ""
    return sentince

def count_vowels(text):
    text = text.lower()
    output = 0
    for c in text:
        for v in "aeiou":
            if c == v: output += 1
    return output

def find_longest_word(text):
    word = ""
    priv_word = ""
    for c in text:
        if c != " ": word += c
        else:
            if len(word) > len(priv_word):
                priv_word = word
                word = ""
            else: word = ""
    return	priv_word

def is_palindome(text):
    revers_string = ""
    for c in range(len(text), 0, -1):
        revers_string += text[c - 1]
    if revers_string == text: output = True
    else: output = False
    return output

print("Reversed text:",reverse_words(user_string))
print("Vowel count:", count_vowels(user_string))
print("Longest word:", find_longest_word(user_string))
print("Is palindrome:", is_palindome(user_string))