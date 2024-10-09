'''
seperate out words 

get top 10 used word ?
how offten used?

use a set to find keys? 
    more memory?

dicturray where unic word with acurence

find total words?
    use revirs dicruar to add value of keys

how to get the bigest 10?
    revers key with data ?
    use max()? 
'''

#main funktion
def main():
    text = loud_text_file("/home/vincentl/Documents/LNU/LNU_Python_Corse/Homework3_part2/GostaBerlingsSaga.txt")
    words = find_words(text)
    print(words)

#put text data in var text
def loud_text_file(lokation):
    text = open(lokation)
    my_str = text.read()
    return my_str

def find_words(in_str):
    list_of_all_words = []
    curent_word = ""
    for i in range(len(in_str)):
        if in_str[i - 1].isalpha == True:
            curent_letter = in_str[i - 1]
            print(in_str[i - 1])
            curent_word += curent_letter
        else: 
            print(curent_word)
            list_of_all_words.append(curent_word)
            curent_word = ""
    return list_of_all_words

main()