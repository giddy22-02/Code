# This program is able to convert temperature from kelvin to degrees Celsius
# and vice versa
# Author: Gideon Kiplangat
# Check the type of the input
inp_typ = int(input('Your Temperature is in Kelvin or celsius? Type 1 for Kelvin and 2 for Celsius: '))
if inp_typ == 1:
    temp = int(input('Enter the temperature: '))
    temp = temp - 273
    print('That is equals', temp, ' degrees Celsius')
elif inp_typ == 2:
    temp = int(input('Enter the temperature: '))
    temp = temp + 273
    print('That is equals', temp, 'Kelvin')
else:
    print("You entered an invalid Temperature")




