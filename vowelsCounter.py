#incomplete/incorrect output for the module
def composite_ratio(the_num):
    ratio_Count = 1
    factor_num = the_num
    if factor_num // ratio_Count == 0:
        ratio_Count += 1         
    return (the_num // ratio_Count)

def add_em_up(bottom, top):
    add_num = 0
    for num in range(bottom, top):
    #For each iteration of the for loop, the value of add_num
    #increases, so the if statement determines whether of not
    #to stop the loop when bottom is greater that top.
        if bottom < top:
            add_num += 1
            bottom += add_num
        else:
            return add_num - 1
    #Returns the total amount of times the loop repeated in the
    #form of add_num.
    return add_num

def vowels_count(letters):
    #Sets Vowel to zero so that when it get to the for loop,
    #it can start adding 1 everytime it sees the designated
    #vowel (a, e, i, o, u).
    a_Vowel = 0
    e_Vowel = 0
    i_Vowel = 0
    o_Vowel = 0
    u_Vowel = 0
    #Sets Count to zero and will be altered each time a new
    # heighest number is reached. Char is set to an empty string
    #and will be altered in relation to Count.
    vowel_Count = 0
    vowel_Char = ' '
    #for statement that repeats for the number of values
    #in the given list
    for l in letters:
    # 1a) For each if statement, the for loop runs through the list
    #provided, for each designated vowel detected by the first if
    #statement, the Vowel variable has 1 added to it.
        if l == 'a' or l == 'A':
            a_Vowel += 1
        #1b) For each the second if statements, if the value of the Vowel
        #variable is the highest value, is now the value for Count
        #and the vowel is now the new Char.
            if a_Vowel > vowel_Count:
                vowel_Count = a_Vowel
                vowel_Char = 'a'
        #1a
        elif l == 'e' or l == 'E':
            e_Vowel += 1
            #1b
            if e_Vowel > vowel_Count:
                vowel_Count = e_Vowel
                vowel_Char = 'e'
        #1a
        elif l == 'i' or l == 'I':
            i_Vowel += 1
            #1b
            if i_Vowel > vowel_Count:
                vowel_Count = i_Vowel
                vowel_Char = 'i'
        #1a
        elif l == 'o' or l == 'O':
            o_Vowel += 1
            #1b
            if o_Vowel > vowel_Count:
                vowel_Count = o_Vowel
                vowel_Char = 'o'
        #1a
        if l == 'u' or l == 'U':
            u_Vowel += 1
            #1b
            if u_Vowel > vowel_Count:
                vowel_Count = u_Vowel
                vowel_Char = 'u'
    #result gathers the Count and Char maxes and puts them in the required
    #format.
    result = "Most Frequent: '" + vowel_Char + "' Count: " + str(vowel_Count)
    return result
        

def wacky_factors(f_list, big_list):
    factorTotal = 0
    #need a double for loop to detect the values in the big list
    #and the small list.
    for num in big_list:
        for fac in f_list:
            #If statement determines whether or not the value in
            #little big list is a factor of f list. If so, 1 is
            #added to the factorTotal
            if num % fac == 0:
                factorTotal += 1
    #Returns the final result of factorTotal         
    return factorTotal
