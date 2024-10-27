'''
find long words
    add amount 

find amount of sentences

caluculate LiX
'''

#main funktion
def main():
    #text = loud_text_file("/home/vincentl/Documents/LNU/LNU_Python_Corse/Homework3_part2/test.txt")
    text = loud_text_file("/home/vincentl/Documents/LNU/LNU_Python_Corse/Homework3_part2/GostaBerlingsSaga.txt")    
    words = find_words(text)
    total_length = find_total_length(words)
    total_long_words = find_amount_of_long_words(words)
    total_sentences = find_sentences_amount(text)
    uniqe_words = get_uniqe_words(words)
    quantety = quantantety_of_word(uniqe_words,words)
    moust_used = top_10_used_words(quantety)
    LIX = calculate_LIX(words,total_sentences,total_long_words)
    output(total_length, moust_used, quantety,total_sentences, total_long_words, LIX)
    

#put text data in var text
def loud_text_file(lokation):
    text = open(lokation)
    my_str = text.read()
    return my_str

def find_words(book):
    #remove special characters
    book_no_spacel_c = ""
    book = book.replace("\n"," ")
    book = book.lower()
    for i in range(len(book)):
        c = book[i - 1]
        if c.isalpha() == True or c == " " or c.isnumeric() == True:
            book_no_spacel_c += chgkpkb-afgwp,pf


    #seperate book in to list of words
    list_of_all_words = []
    curent_word = ""
    for i in range(len(book_no_spacel_c)):
        c = book_no_spacel_c[i - 1]
        if c.isalpha() == True or c.isnumeric() == True :
            curent_word += c
        else: 
            if curent_word != "": list_of_all_words.append(curent_word)
            curent_word = ""

    return list_of_all_words

def find_total_length(all_words):
    return len(all_words)

def get_uniqe_words(all_words):
    return set(all_words)

def quantantety_of_word(keys, all_words):
    #create dicturnarry where every uniqe word has the ammount assotionated
    ammount_per_word = {x:0 for x in keys}
    
    #adds amount of a word to the dicturnarry
    for word in all_words:
        ammount_per_word[word] += 1
    
    return ammount_per_word

def top_10_used_words(quantety):
    top_10 = []
    top_10_dic = {}
    #go thrue 10 times
    for i in range(10):
        bigest = 0
        bigest_key = ""
        for e in quantety:
            to_test = quantety.get(e)
            if to_test > bigest:
                bigest = to_test
                bigest_key = e
        #remove bigest to find second bigest & add values
        top_10.append(bigest_key)
        top_10_dic.update({bigest_key:bigest})
        quantety.pop(bigest_key)    
    #add backe values to mack working eseayer
    quantety.update(top_10_dic)
    return top_10 

def find_amount_of_long_words(words):
    long_words = 0
    for word in words:
        if len(word) > 6:  long_words += 1
    return long_words

def find_sentences_amount(text):
    amount_of_sentences = 0
    for c in text:
        if c in ".!?": amount_of_sentences += 1
    return amount_of_sentences

def calculate_LIX(total_words,total_sentences,total_long_words):
    return (len(total_words)/total_sentences + (total_long_words/len(total_words) * 100))

def output(total_words, moust_used, quantety,total_sentences,total_long_words,LIX):
    print("Information about Gösta Berlings Saga")
    print(f"Total number of words: {total_words}")
    print(f"Total sentences: {total_sentences}")
    print(f"Long words(>6 characters): {total_long_words}")
    print(f"LIX (Swedisch Readability Index): {LIX}")
    print()
    print("Ten moust common words:")
    for i in range(10):
        print(f"{moust_used[i]:<8} {quantety.get(moust_used[i])}")
main()