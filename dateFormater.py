def reformatDate(date):
    dt = date.split()
    day = date[0:2]
    month_set = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
    try:
        if (((int(day) <= 31) and (int(day) >= 1)) == False):
            raise ValueError
        elif ((len(dt[2]) > 4) == True):
            raise ValueError
        elif ((dt[1] in month_set) == False):
            raise ValueError
        print("Date is: " + dt[2] + "-" + dt[1] + "-" + day)
    except ValueError:
        print("The input is invalid")



