# Barbara Presley
# Program:  Awesome Temperature Converter
# This program uses functions to perform temperature conversions
# and allows the user to chose different conversions from a menu

print (f'The Awesome Temperature Converter') #welcome message

# Constants for the menu choices
TO_FAHR_CHOICE = 1
TO_CELS_CHOICE = 2
QUIT_CHOICE = 3

#The main function.
def main():
        # The choice variable controls the loop
        # and holds the user's menu choice.
        choice = 0

        while choice != QUIT_CHOICE:
                # Display the menu.
                display_menu()

                # Get the user's choice:
                choice = int(input('\nEnter your choice: '))

                # Perform the selected action
                if choice == TO_FAHR_CHOICE:
                        
                        #Get values for conversions
                        ctemp = float(input('Enter the Celsius temperature to convert: ')) 
                        #validate input is not less than absolute zero (-273.15 degrees C)
                        while ctemp <-273.15:
                            print('\nError! -temp below absolute zero :( Please reenter!')
                            ctemp = float(input('\nEnter the Celsius temperature to convert: '))
                        def to_fahr(num1, num2):
                                result = 9/5 * ctemp + 32
                                return result
                        print('\n(ctemp) degrees Celsius is (result) degrees Fahrenheit.')

                # Perform the selected action
                elif choice == TO_CELS_CHOICE:
                        #Get values for conversions
                        ftemp = float(input('Enter the Fahrenheit temperature to convert: ')) 
                        #validate input is not less than absolute zero (-273.15 degrees C)
                        while ftemp <-459.67:
                            print('\nError! -temp below absolute zero :( Please reenter!')
                            ftemp = float(input('\nEnter the Celsius temperature to convert: '))
                        def to_cels(num1,num2):
                                result = (ftemp-32) * 5/9
                                return result
                        print('\n (ctemp) degrees Fahrenheit is (result) degrees Celsius.')

                # Exiting the program
                elif choice == QUIT_CHOICE:
                        print('Thank you for using this program!')

# The display_menu function displays a menu.
def display_menu():
        print('\nMENU')
        print('\n1) Convert Celsius to Fahrenheit')
        print('2) Convert Fahrenheit to Celsius')
        print('3) Quit')
                                
#Call the main function
main()


        
