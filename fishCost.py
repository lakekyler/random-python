def calculate_price(a_type, month, bass_price):
    tax = 0
    mark_up = 0
    if a_type != 'fish':
        return(print('entered animal is incorrect'))
    if month == 'october':
        mark_up = .08
        tax = .04
    elif month == 'november':
        mark_up = .1
        tax = .05
    elif month == 'december':
        mark_up = .12
        tax = .065
    elif month == 'january':
        mark_up = .18
        tax = .067
    else:
        return(print('entered month is incorrect'))
    bass_pri = bass_price
    bass_price = bass_price * mark_up
    bass_price = bass_pri + bass_price
    bass_pri = bass_price
    bass_price = bass_price * tax
    bass_price = bass_pri + bass_price
    return print('Final Price is: $'+ str(bass_price))


