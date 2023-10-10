print (f'Welcome to Super Scoops Ice Cream!') #welcome message

scps = int(input('How many scoops would you like? ' ))
#int input quanity of ice cream scoops
if scps <1: #conditional test for invalid values
    # if scps is <1, only a response to the customer will be printed
    # no calculations performed or advancement to the next question
    print(f'You asked for {scps} scoops. You must order one or more scoops.')	
    print (f'\nThank you for using this program!') #goodby message

    ##I tried to set up a boolean test for the waffle cone
    ##but couldn't get it to work
    ##please see below:
    ##else #move forward with order collection
    ##wafl = bool(input('Would you like a waffle cone?  y/n: ' ))
    ##if wafl = y
    ##want_wafl = True
    ##else: want_wafl = False
    ## collect waffle cone order
    ##if want_wafl = True: #value test
    ##print (f'Thanks for using this program!') #goodby message 

elif scps <3:
#conditional test for 1-2 scoop prices
    ppS =  1.5
    #price per scoop if 1 or 2
    total = (scps * ppS)  
    print(f'\nThe price per scoop is: ${ppS:2,.2f}')
    print(f'You ordered: {scps:2,}')
    print(f'Your total cost is: ${total:2,.2f}')
    print('\nThank you for using this program!')

else: scps >= 3
    #conditional test for 3 or more scoops
d_ppS = 1.25
#discounted price per scoop if more than two
#calculate the scoops times the price per scoop
total = (scps * d_ppS)
#calculate the scoops times the price per scoop
print(f'\nThe price per scoop is: ${d_ppS:2,.2f}')
print(f'You ordered: {scps:2,}')
print(f'Your total cost is: ${total:2,.2f}')
print('\nThank you for using this program!')
