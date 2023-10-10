# Barbara Presley
# Lab 4, CMSY-156_091
# This program demonstrates a while loop
# and a for loop
# to perform temperature conversions.




cels = int(input('Enter in the starting temperature: '))
# gather starting temperature
while cels < -233.15:
        print('Error! Temperatures cannot be below absolute zero.  Please reenter!')
        cels = int(input('\nEnter in the starting temperature: '))
cels = cels + 1
fahr = ((9/5) * cels + 32)
#convert celcius to Fahr
kelvin = cels + 273.15
# convert celcius to kelvin

# This section uses a while loop to display
# A series of temperature conversions


# MAX_TEMP = cels + 20
# setting the maximum value
# the program to iterate 20 times

# Print the table headings.
print('Cels\tFahr\tKelvin')
print('------------------')
print('Note: I cant seem to get cels to iterate')
print('adding 1 to the value of the input value :(')

# while cels < MAX_TEMP
# setting the maximum value
# the program to iterate 20 times
# print(f'{cels:2,.2f}\t{fahr:2,.2f}\t{kelvin:2,.2f}')

# This section uses a for loop to display
# A series of temperature conversions

# Print the table headings.
print('\nCels\tFahr\tKelvin')
print('------------------')

# Use a for loop to
# Convert the user Celsisus values into
# Fahrenheit and Kelvin

cels = (cels + 1)
for cels in range(21):
# Setting repeater values
        print(f'{cels:2,.2f}\t{fahr:2,.2f}\t{kelvin:2,.2f}')
        
print (f'\nThanks for using this program!') #goodby message










