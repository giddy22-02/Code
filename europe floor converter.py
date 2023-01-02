# This program is able to tell the user the equivalent floor number is either
# USA or Europe, depending on the location of the user
# Author: Gideon Kiplangat
# Check the location of the user
location = int(input('Are you in Europe or USA? Type 1 for Europe and 2 for USA: '))
if location == 1:
    print('Welcome to Europe!')
    floorNumber = int(input('Enter Your Floor No: '))
    usaFloorNumber = floorNumber + 1
    print('That is equals to USA floor No', usaFloorNumber)
elif location == 2:
    print('Welcome to USA!')
    floorNumber = int(input('Enter Your Floor No: '))
    EuropeFloorNumber = floorNumber - 1
    print('That is equals to Europe floor No', EuropeFloorNumber)
else:
    print("Invalid Location")




