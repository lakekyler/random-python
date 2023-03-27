def check_correctness(*numbers):
    new_list = []
    for l in numbers:
        new_list.append(l)
    sum_val = sum_list(new_list)
    result = ones_digit(sum_val)
    if result == new_list[-1]:
        return 'correct'
    else:
        return 'error'
    
def sum_list(lst):
    value = 0
    for i in range(len(lst)):
        value += lst[i]
    value -= lst[-1]
    return value

def ones_digit(number):
    one_dig = number % 10
    return one_dig


    



