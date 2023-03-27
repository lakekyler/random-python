def findRecommendations(matches):
    #copies and clears the values for matches
    copy = matches.copy()
    matches.clear()
    #will be used and discussed later
    highest_match = -1
    #range determines by the interval of where the ints are
    #in this case, they are in intervals of three so the range
    #needs to be read in intervals of three
    #(0, 3, 6, etc. depending on length of list)
    for i in range(0, len(copy), 3):
        #gets the integers from the interval in the range
        #(2, 5, 8, etc. depending on the length of the list)
        if copy[i + 2] >= 80:
        #if the int values were greater than or equal to 80, the int
        #and the previous values it represents is appended to matches
        #(the number (ex. 90) would be appended with its values (ex. 'JS', 'M')
            matches.append(copy[i : (i + 3)])
            #determines whether or not a new value in the matches list is the new
            #"highest match". This is determined by comparing the new integer in
            #copy to the value in matches
            if copy[2] > matches[highest_match][2] or  highest_match == -1:
            #if the new copy integer is greate than the old value, then the
            #value of highest match changes.
                highest_match = len(matches) - 1
    #appends the heart shape to the highest match list
    if highest_match != -1:
        matches[highest_match].append('\u2665') 


def compressInfo(datingTrack):
    #copies and clears the values for datingTrack
    copy = datingTrack.copy()
    datingTrack.clear()
    #goes through each value of copy
    for i in copy:
        for j in range(len(datingTrack)):
            #if the id for datingTrack is equal to the id of the current
            #value of 'i'
            if i[0] == datingTrack[j][0]:
                #sets the second value of datingTrack to an integer
                #that is either added to as the for loop goes through
                #its process, or remains the same as to loop continues
                datingTrack[j] = (datingTrack[j][0],datingTrack[j][1]+1)  
                break
        else:
            #for if there is not another value for the current datingTrack
            #value, it is defaulted to 1
            datingTrack.append((i[0],1))


def combineInfo(profileInfo, datingTrack):
    #sets the range to the length of profileInfo
    for i in range(len(profileInfo)):
        #sets the range to the length of datingTrack, which is
        #SMALLER than profileInfo, which is why its in the
        #profileInfo range
        for j in range(len(datingTrack)):
            #determines if the second value of the current
            #profileInfo is equal to the first value of
            #the current datingTrack
            if profileInfo[i][1] == datingTrack[j][0]:
                #if the statement if true, the integer appends to
                #the profileInfo list 
                profileInfo[i].append(datingTrack[j][1])


def setofNames(profiles, location):
    #sets return value to a set, which will be
    #able to store the values in the upcoming
    #for loop
    mem_names = set()
    #scans all the values in profiles in order
    for i in profiles.values():
        #determines if the 3 value in the current
        #is equal to the location value given by the user
        if i[2] == location:
            #if it is, the name values ([0]) is ADDED
            #to the set mem_names
            mem_names.add(i[0])
    #mem_names is returned with all the names added to it
    return mem_names

