#user inputs
original_msrp = int(input('MSRP at time of buying: '))
year = int(input('Manufacture year: '))
miles = int(input('Miles driven: '))
accidents = int(input('Number of accidents reported: '))
current_year = 2022 #current year given to us
msrp = original_msrp #for accidents use

#code for to determine msrp after taking price of how old it is
if current_year > (year + 3):
    msrp = msrp - (500 * (current_year - year))
else:
    msrp -= 0

#code to determine msrp after taking price of miles driven
if miles > 50000:
    msrp = msrp - (100 * (miles/1000))
elif miles < 50000:
    msrp = msrp - (50 * (miles/1000))
else:
    print('error')

#code to determine msrp after taking price of accidents
if accidents != 0:
    msrp = msrp - (accidents * (.10 * original_msrp))
else:
    msrp = msrp

#output of final code
print('Value of vehicle: $' + str(msrp))
    
