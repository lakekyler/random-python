def find_word_values_list(words_list, letter_points_dct):
    value = 0
    word_points_list = []
    #Takes each word of the list
    for i in words_list:
    #Determines the index of each word
        for j in range(len(i)):
    #Takes the key from the dict
            for k in letter_points_dct:
    #Compares the words/index of words to the current value of k
                if i[j] == k:
                    value += letter_points_dct[k]
    #Appends the values of 'value' to a list
        word_points_list.append(value)
    #Resets value for each loop
        value = 0
    return word_points_list
        
