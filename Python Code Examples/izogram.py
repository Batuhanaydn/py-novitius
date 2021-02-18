def is_isogram(word): 
    clean_word = word.lower() 
    letter_list = [] 
    for letter in clean_word: 
        if letter.isalpha(): 
            if letter in letter_list: 
                return False
            letter_list.append(letter) 
    return True
  
if __name__ == '__main__': 
    print(is_isogram("Machine"))                              
    print(is_isogram("isogram"))                          
    print(is_isogram("Alphabet")) 
    print(is_isogram("kea"))