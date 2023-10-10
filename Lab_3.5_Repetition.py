#This program calculates soccer scores
print (f'Welcome to the Most Awesome '
	'CMSY-156_091 Soccer Calculator') #welcome message

another = 'y' #Variable to control the loop
while another =='y' or another == 'Y':
    #Gather soccer score inputs

    sum_gms_plyd = float(input('Enter the number of games: ')) 
    #validate the games played
    while sum_gms_plyd <0:
        print('Error!  The games cannot be negative :(')
        sum_gms_plyd = float(input('Please enter the correct number of games: '))
    if sum_gms_plyd == 0: #conditional test for 0 value
    # if sum_gms_plyd is 0, only this variable will be printed
    # no calculations performed, only printing sum_gms_plyd for each answer
        print(f'The average goals per game is: {sum_gms_plyd:10,.2f}')	
        print(f'The average shots per game is: {sum_gms_plyd:10,.2f}')
        print(f'The average shots per goal is: {sum_gms_plyd:10,.2f}')
        print (f'Thanks for using this program!') #goodby message 
    else: #data will be captured and calculations performed
        sum_sht_tkn = float(input('Enter the number of shots taken: '))
        #validate the shots taken
        while sum_sht_tkn <0:
            print ('Error!  The shots cannot be less than zero :(')
            sum_sht_tkn = float(input('Please enter the correct number of shots: '))
            #float input sum shots taken
        sum_gls_scrd = float(input('Enter the number of goals made: '))
        #validate the goals scored
        while sum_gls_scrd <0:
            print ('Error! The goals cannot be less than zero :(')
            sum_gls_scrd = float(input('Please enter the correct number of goals: '))
        #float input sum goals scored
        if sum_gls_scrd == 0: #conditional test for 0 value
        # if sum_gls_scrd is 0, no calculations relevant to this will be performed
        # sum_gls_scrd as  0 will replace avg goals per game
        # sum_gls_scred as 0 also replaces avg shots per goal
        # no calculations performed, only printing sum_gms_plyd for each answer
            print(f'The average goals per game is: {sum_gls_scrd:10,.2f}')
            #replaces 0 sum_gls_scrd with calculation
            avg_sht_p_gm = (sum_sht_tkn / sum_gms_plyd)
            #float find average as sum goals \
            #scored divided by sum games played
            print(f'The average shots per game is: {sum_gms_plyd:10,.2f}')
            print(f'The average shots per goal is: {sum_gls_scrd:10,.2f}')
             #replaces 0 sum_gls_scrd with calculation
            print (f'Thanks for using this program!') #goodby message
        else: #full data will be captured and calcuations performed.
            ##Calculate the average goals per game
            avg_gls_p_gm =  (sum_gls_scrd / sum_gms_plyd)
            #float find average as sum goals * sum games \
            #divided by sum games played
            avg_sht_p_gm = (sum_sht_tkn / sum_gms_plyd)
            #float find average as sum goals \
            #scored divided by sum games played
            avg_sht_p_gl = (sum_sht_tkn / sum_gls_scrd)
            #float find average as sum goals scored \
            #divided by sum games played
            print(f'The average goals per game is: {avg_gls_p_gm:10,.2f}')	
            print(f'The average shots per game is: {avg_sht_p_gm:10,.2f}')
            print(f'The average shots per goal is: {avg_sht_p_gl:10,.2f}')
            # displaying calculated values avg goals per game, \
            #avg shots per game, \
            #avg shots per goal \
            #and round to two decimal points

            # Do this again?
            another = input('\nWould you like to enter another (y/n)?')
            ##Not sure how to validate another
            ##if another != ('y, Y, n, N')
               ## print ('Error!  You must enter y or n :( ')
                ##else: 
                ##another = float(input('\nWould you like to enter another (y/n)?')
            ##not sure how to validate text
            ##use a list???  something like:
            ##while another not in ['y or Y or n or N']??
            ##anything else, display error message -
            ##still need to validate between a "N" entry and an invalid
            if another == 'n' or another == 'N':
                print (f'Thanks for using this program!') #goodby message
            

