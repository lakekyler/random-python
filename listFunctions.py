def indices(some_list, another_list):
    #list for final return
    final_lst = []
    #sets range to the length of the first list
    for i in range (0, len(some_list)):
    #compares the values of list 1 and list 2
    #to determine of they are the same
        if some_list[i] == another_list[i]:
    #if they are the same, the value of i is appended
    #to the empty list
            final_lst.append(i)
    return final_lst


def compute(lst1, lst2, lst3):
    #list for final return
    final_lst = []
    for i in range(0, len(lst1)):
        #if the boolean is true, the specific values from
        #list 1 and 2 are added and appended to the final list
        if lst3[i] == True:
            value = lst1[i] + lst2[i]
            final_lst.append(value)
        #if the boolean is false, the specific values from
        #list 1 and 2 are subtracted and appended to the final list
        elif lst3[i] == False:
            value = lst1[i] - lst2[i]
            final_lst.append(value)
        else:
            final_lst.append('error')
    return final_lst


def replace_elems(lst1, lst2, n):
    #list for final return
    final_lst = []
    #loop for if list 1 is greater than list 2
    #final_lst is set to smaller list
    if len(lst1) > len(lst2):
        final_lst = lst2
        for i in range(n-1, len(lst2), n):
            #changes the value of final_Lst in intervals of the
            #given 'n' value
            final_lst[i] = lst1[i]
    #loop for if list 2 is greater than list 1
    #loop has exactly the same as function as the previous list,
    #the lists were just swapped
    else:
        final_lst = lst1
        for i in range(n-1, len(lst1), n):
            final_lst[i] = lst2[i]
    return final_lst


def extra_copies(some_list):
    dupes = 0
    for i in range(len(some_list)):
        j = i - 1
        if some_list[i] == some_list[j - 1]:
            dupes += 1
    return dupes






