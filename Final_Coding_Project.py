#This program asks the user to input a list name
#Reads the list, inspecting for suspect IP Addresses
#Produces an output including:
#1) number of records in file, 2) Percentage of suspect IP's, and 3) List of suspect IP's & timestamp



def main():
    #This is going to do something cool
    print(f'Welcome to CMSY Final Coding Project!')
    print('Barbara Presley, Summer 2023')

    #placeholder variables for working with the data
    list1 = 0
    list2 = 0

    def read_file():
    #read_file function gets the file name from the user
    #uses a try/except handler to make sure a valid file name is entered
    #reads the file, stores it as a list
    #and closes the file

        #Get the file name from the user
        file_name = str(input('\nEnter the input file name: '))
        
        list1 = []
        #list one will receive the file data
        #and store it in a list
        try:
            #open the file for reading
            ip_file = open(file_name,'r')

            #process file
            line = ip_file.readline()

            while line != '':
                list1.append(line.rstrip('\n'))
                line = ip_file.readline()

            #Close the file
            ip_file.close()

        except:
            print('ERROR -- There is an issue with file file',file_name,'. Please reenter:')

        #tested to make sure file read was successful
        #print(list1)

    read_file()

    def output_report():

        #use the list.copy method to create a new list as a copy
        #list2 = []
        #list2 = list1.copy()

        #This is where I've gotten stuck
        #I'm not sure if I didn't loop through the file correctly when it was read
        #or if something went wrong going from list1 (all data from read function)
        #to list2 - a second this copied for to show the outputs and handle required operations/sorting

        #The outputs would go something as follows:
        print('\n1)This is where I should display the length of the list.')
        print('using a function such as len_list = [len(S) for s in str_list')

        #The second output should be something like this:
        print('\n2) This is where I should have used a For function to read through the 2nd list')
        print('It would just the suspect IP addresses as search values')
        print('It would then need to store this output as a variable')
        print('and print the identified IP addesses with proper formating & sorting')

        #The IP addresses need to be sorted, which would need to be done in a manner like this:
        #sorting:
        #print('Original order:' my_list)
        #my_list.sort()
        #print('Sorter order:' my_list)

        #Finaly, a percentage value is being requested
        print('\n3) This is where I would need to provide the percentage of suspect IP addresses')
        #I beleive to do this, I would create a variable for the length of list one (first list with all data)
        #and have a variable for the length of list two (both stored as float)
        #then divide length of list2 by list1, and format the display to three decimal places
    
    output_report()

    #def list_function(list):
        #for x in list:
            #print(x)

        #list = [ip_file]
    #list_function(list)

    print('\nThank you for using this program!')



#call the main function
main()
