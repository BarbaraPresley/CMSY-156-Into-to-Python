#This program calculates soccer scores
print (f'Welcome to the Most Awesome '
	'CMSY-156_091 Soccer Calculator') #welcome message

# This program demonstrates uses the return value of a function

def main():
    #establishing a variable to control the loop
    #Note: having trouble with the setup of the control loop here & at the end
    #another = 'y'
    #while another =='y'

        #Get the number of games
        in_games = float(input('Enter the number of games: ')) 
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

        #Get the average goals per game
        #Average is number of goals divided by number games
        avg_glpgm =  average(in_goals, in_games)

        #Get the average shots on goal per game
        #Average is number of shots taken divided by number games
        avg_spgm = average(in_shots, in_games)

        #Get the average shots per goal
        #Average is number of goals divided by number games
        avg_spgl = average(in_shots, in_games)

        #The average function accepts two numeric arguments
        #divides the first value by the second value
        #and returns the average

        #Display the averages
        print(f'The average goals per game is: {avg_glpgm:10,.2f}')	
        print(f'The average shots per game is: {avg_spgm:10,.2f}')
        print(f'The average shots per goal is: {avg_spgl:10,.2f}')

def average(num1, num2):
    result = num1 + num2
    return result        

#Do this again?
#another = input('\nWould you like to enter another (y/n)?')
#if another !='y'
#print (f'Thanks for using this program!') #goodby message

#Call the main function
main()


        
