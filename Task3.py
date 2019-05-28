#To find the length of the longest word
def find_longest_word(words_list):  
    word_len =[]
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()
    print("The longest word is:",word_len)
    return word_len[-1][1]  

print(find_longest_word(["car", "bike", "scooter"])) 
