#This program will do several things....
#It will use seven functions

#constants for the menu choices
SCORE_METRICS = 1
MINE_SCORES = 2
UPDATE_SCORE = 3
DISPLAY_SCORES = 4
QUIT = 5
NUM_SCORES = 0

#The main function
def main():
        print (f'Welcome to Lab 7 - the last lab of the Class!') #welcome message

        #Get the user to determine how many scores will be entered
        NUM_SCORES = int(input('\nHow many scores will you be entering? '))

        #create a list to hold test scores
        input_scores = [0] * NUM_SCORES

        print('Enter the test scores')

        # Get the test scores
        for index in range(len(input_scores)):
                input_scores[index] = float(input(f'Enter test score{index + 1}(0-100): '))
        #Display the values entered
        print('Here are the values you entered:')
        for value in input_scores:
                print (value)

        #The choice variable controls the loop
        #and holds the user's menu choice.
        choice = 0

        def display_menu():
                print('\n1 = Score Metrics (min/max/avg)')
                print('2 = Mine Scores (low/high scores)')
                print('3 = Update Score')
                print('4 = Display Scores')
                print('5 = Quit')

        while choice != QUIT:
                #display the menu.
                display_menu()

                #get the user's choice
                choice = int(input('\nPlease make a selection: '))

                #Perform the selected action
                if choice == SCORE_METRICS:
                    def score_metrics():
                            pass
                    print('Unfortunately I ran out of time')
                    #This is where one would find and display the highest and lowest test scores
                    #Also calculate and display the average test score
                
                elif choice == MINE_SCORES:
                        def mine_scores():
                            pass
                            print('Unfortunately I ran out of time')
                    #This is where one would use list comprehensions to create two new lists and display them
                    # One with scores greater than or equal to the average score
                    # One with scores less than the average score
                    # Each list should be sorted to display the scores in ascending order
                    
                elif choice == UPDATE_SCORE:
                        def mine_scores():
                            pass
                            print('Unfortunately I ran out of time')
                    # This is where one display test scores numbered
                    # Prompt the user to update
                    # Test for an invalid entry / allow re-entry
                    # Update the selected socre (by index)
                    # Redisplay the test scores after the update.
                    # One with scores less than the average score
                    
                elif choice == DISPLAY_SCORES:
                        def display_scores():
                            pass
                            print('Unfortunately I ran out of time')
                    # This is where one display test scores in reverse order
                    # using a slice operation with negative indices
                    
                elif choice == QUIT:
                        print('Thank you for using this program!')
                  
#Call the main function
main()


        
