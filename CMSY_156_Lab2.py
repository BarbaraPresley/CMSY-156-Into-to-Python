print (f'Cell Phone Calcuator') #title line

#Input Variables
mk_mdl = (input('Enter in cell phone make and model: ')) 
#float input cell make and model

ph_c = float(input('Enter in the price of the phone in dollars: $')) 
#float input price of the phone

wrnty_c = float(input('Enter in the price of the warranty in dollars: $'))
#float input warranty price

#Calculated Variables

s_tax = float((ph_c + wrnty_c) * 0.06)
#calcuate sales tax

sh_c = float(0.017 * wrnty_c)
#calcuate shipping cost

total = float(ph_c + wrnty_c + s_tax + sh_c)
print()
    #inserting space. I tried using \n
    #but couldn't get it to work
print('Receipt: ') #receipt header
	
print(f'The purchase price is: ${ph_c:.2f}.')
	#display the purchase price
print(f'The warranty cost is: ${wrnty_c:.2f}.')
	#display the warranty cost	
print(f'The tax is: ${s_tax:.2f}.')
	#display the sales tax
print(f'The shipping cost is: ${wrnty_c:.2f}.')
	#display the shipping cost
print()
print (f'Have a good day!') #goodby message 

