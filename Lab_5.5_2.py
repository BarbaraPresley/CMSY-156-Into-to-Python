#This program reads names from two different files and writes them to a new file.


#Download: nameslist1.txt
#Download: nameslist2.txt

def main():
        #Read the contents of the soccer.txt file one at a time
        names_1 = open('nameslist1.txt.', 'r')

        #NOTE: when calling the [:-1] function, received error:
        #TypeError: '_io.TextIOWrapper' object is not subscriptable
        #soccer_file = soccer_file[:-1]
        
        #Read three lines from the file
        line1 = names_1.readline()
        line2 = names_1.readline()
        line3 = names_1.readline()
        line4 = names_1.readline()

        print('\n')
        print('First Name: ',line1)
        print('Last Name: ')
        print(line2)
        print('Team Name: ')
        print(line3)
        print('League: ')
        print(line4)
        print('\nEnter info for:')
        print(line1)
        print(line2)

        #Close the file
        nameslist1.close()

    #establishing a variable to control the loop
    #Note: having trouble with the setup of the control loop here & at the end
        another = 'y'
        while another == 'y' or another =='Y':

                #Get the number of games
                in_games = float(input('\nEnter the number of games: ')) 
                #validate the games input
                while in_games <0:
                    print('Error!  The games cannot be negative :(')
                    in_games = float(input('Please enter the correct number of games: '))

                #Get the number of shots taken
                in_shots = float(input('Enter the number of shots taken: '))
                #validate the shots taken
                while in_shots <0:
                    print ('Error!  The shots cannot be less than zero :(')
                    in_shots = float(input('Please enter the correct number of shots: '))

                #Get the number of goals
                in_goals = float(input('Enter the number of goals made: '))
                #validate the goals scored
                while in_goals <0:
                    print ('Error! The goals cannot be less than zero :(')
                    sum_gls_scrd = float(input('Please enter the correct number of goals: '))



                #Display the averages
                print(f'The average goals per game is: {avg_glpgm:10,.2f}')	
                print(f'The average shots per game is: {avg_spgm:10,.2f}')
                print(f'The average shots per goal is: {avg_spgl:10,.2f}')

                #Do this again?
                another = input('\nWould you like to enter another (y/n)?')
                if another != 'y':
                        print (f'Thanks for using this program!') #goodby message

def average(num1, num2):
    result = num1 + num2
    return result        

#Call the main function
main()


        
