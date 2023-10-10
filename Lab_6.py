#Barbara Presley
#This program is an attempt at a program
#That would prompt the user to identify two input files
#And an output file location, then combine the two inputs.
#The Try/Except function is used to intercept incorrect input
#And prevent crashes


print (f'Welcome to Lab 6 - Files & Exceptions') #welcome message

#This program 

def main():
        try:
                #Get the file name of the first file to open
                input_1 = input('\nEnter the path and name of the first file: ')
                #use error handler to prompt the user to try again
        except ValueError:
                print('Error: file(s) not found, or could not be opened.')
                print('Please reenter')
                input_1 = input('\nEnter the path and name of the first file: ')

        #Open the first file
        names_1 = open('nameslist1.txt', 'r')

        # Read the first line from the file
        # and check for an empty string
        line = names_1.readline()

        # As long as an empty string is not returned
        # from readline, continue processing
        while line != '':
                print(line)

                #read the next line
                line = names_1.readline()
                #Strip the newlines from the field
                line = line.rstrip('\n')

        #At some point in this process, I think you would want to
        #Create a temporary file and write the records from names1 to this file
        #But I am not sure how

        #Close the file
        names_1.close()
                           
        try:
                #Get the file name of the second file to open
                input_2 = input('\nEnter the path and name of the second file: ')
                #use error handler to prompt the user to try again
        except ValueError:
                print('Error: file(s) not found, or could not be opened.')
                print('Please reenter')
                input_1 = (input('\nEnter the path and name of the second file: ')
                
       try: 
                #Get the file name of the first file to open
                output_file = input('\nEnter the path and name of the output file: ')
                #use error handler to prompt the user to try again
        except ValueError:
                print('Error: Invalid path and file name.')
                print('Please reenter')
                input_1 = (input('\nEnter the path and name of the output file: ')

        # Processing message
        print('Names processing started')

        #Open the second file
        names_2 = open('nameslist2.txt', 'r')

        #Read all the lines from the file.
        for line in names_2:
                # Convert line to string
                names_2 = string(line)

        #At this point I think you would want to append the data
        #From names2 to the temporary file
        #And save it to the place defined as output_file
        #But I am not sure how

        print('Names processing complete')
        #Close the file
        names_2.close()

#Call the main function
main()


        
