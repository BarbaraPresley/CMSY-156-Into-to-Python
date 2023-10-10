print (f'Welcome to the Most Awesome '
	'CMSY-156_091 Soccer Calculator') #welcome message
sum_gms_plyd = float(input('Enter the number of games: ')) 
#float input sum games played
sum_sht_tkn = float(input('Enter the number of shots taken: ')) 
#float input sum shots taken
sum_gls_scrd = float(input('Enter the number of goals made: '))
#float input sum goals scored 
##Calculate the average goals per game
avg_gls_p_gm =  ((sum_gls_scrd * sum_gms_plyd) / sum_gms_plyd)
#float find average as sum goals * sum games \
#divided by sum games played
avg_sht_p_gm = ((sum_sht_tkn * sum_gms_plyd) / sum_gms_plyd)
#float find average as sum goals \
#scored divided by sum games played
avg_sht_p_gl = (sum_sht_tkn / sum_gls_scrd)
#float find average as sum goals scored \
#divided by sum games played
print(f'The average goals per game is: {avg_gls_p_gm:.2f}')	
print(f'The average shots per game is: {avg_sht_p_gm:.2f}')
print(f'The average shots per goal is: {avg_sht_p_gl:.2f}')
# displaying calculated values avg goals per game, \
#avg shots per game, \
#avg shots per goal \
#and round to two decimal points
print (f'Thanks for using this program!') #goodby message 
