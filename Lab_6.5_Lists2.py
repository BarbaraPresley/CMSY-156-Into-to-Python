

#This program reads the contents of the soccer.txt file
#demonstrates uses the return value of a function
# and demonstrates passing values into a list

def main():
        #This program calculates soccer scores
        print (f'Welcome to the CMSY Soccer Calculator') #welcome message
        
        def read_file():
        #define a function to open the file and print the header
                soccer_file = open('soccer.txt', 'r')

                #NOTE: when calling the [:-1] function, received error:
                #TypeError: '_io.TextIOWrapper' object is not subscriptable
                #soccer_file = soccer_file[:-1]
        
                #Read four lines from the file
                line1 = soccer_file.readline()
                line2 = soccer_file.readline()
                line3 = soccer_file.readline()
                line4 = soccer_file.readline()

                print('\nFirst Name:',line1)
                print('Last Name:',line2)
                print('Team Name:',line3)
                print('League:',line4)
                print('Enter info for:',line1,line2)

                #Close the file
                soccer_file.close()

        def get_input():

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
                        in_goals = float(input('Please enter the correct number of goals: '))
                

        #Create a function to take the two inputs
        #And return the averages
        def avg_vals(num1,num2):
                avg = num1 / num2
                return avg

        

        def display(d_list):
                #creating a display function
                print('The average goals per game is: ',d_list[0])	
                print('The average shots per game is: ',d_list[1])
                print('The average shots per goal is: ',d_list[2])
    
        
        read_file()
        #call the header function

        in_shots = 0
        in_goals = 0
        in_games = 0
        
        get_input()

        #Average is number of goals divided by number games
        avg_glpgm = avg_vals(in_goals, in_games)

        #Average is number of shots taken divided by number games
        avg_spgm = avg_vals(in_shots, in_games)

        #Average is number of goals divided by number games
        avg_spgl = avg_vals(in_shots, in_games)

        


        
        
        d_list = [0, 0, 0]
        #creating a placeholders for values
        d_list[0] = avg_glpgm
        d_list[1] = avg_spgm
        d_list[2] = avg_spgl
        #passing values into list
        
        display(d_list)
               
        #Do this again?
        #another = input('\nWould you like to enter another (y/n)?')
        #if another != 'y':
                #print (f'Thanks for using this program!') #goodby message        

#Call the main function
main()


        
