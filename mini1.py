
# This script simulates a rolling dice game. It askes user for integer inputs and prints random output number of the user-defined dice. 


# importing packages
import numpy as np



# asking if user is interested in rolling dice
play = raw_input("\nHello user, would you like to roll a dice of your choice ? Kindly answer in 'yes' or 'no' only:\n")

# initializing a variable to limit number of allowable attempts
count = 0

# Restricting number of attempts for correct inputs before existing the game
while ((play.lower() !='yes' and play.lower() != 'no')):
	
	# printing message to user
	print ("\nYou entered incorrect input. Kindly answer in 'yes' or 'no' only:\n")
	
	# increasing attempt by one
	count= count + 1
		
	# printing exiting message
	if count >= 5:
		print ("\n Non cooperative user. Exiting the game.\n")
		exit()
	
	# again asking for correct input
	play = raw_input("\n")

# checking if user is interested in playing
if play.lower() == 'no':
	print ("\nHave a nice day\n")

# Add GUI in the program 

# Method verb and attribute noun


# using while loop for dice roll
while play.lower() == 'yes':
	min = raw_input("\nPlease enter minimum value of a positive integer number on the dice:\n")
	max = raw_input("\nPlease enter maximum value of a positive integer number on the dice:\n")
		
	# Using if else or try/except block to verify input as integer only		
	# Using if-else statements to check correct inputs
	
	if (min.isdigit() and min>0 and (int(min) == float(min)) and max.isdigit() and (int(max) == float(max)) and int(max)>int(min)):
			
		# generating random integer
		rand_int = np.random.randint(int(min),int(max))
		
		# printing ouput
		print('\n')
		print ('The dice rolled:', rand_int)
	
	else:
		print ('\nIt seems that you entered incorrect input. Make sure that input values are in integers only and maximum is larger than minimum')
		
	# asking user again for fresh input	
	play = raw_input('\nWould you like to play again: \n')

	while ((play.lower() !='yes' and play.lower() != 'no')):
	
		# printing message to user
		print ("\nYou entered incorrect input. Kindly answer in 'yes' or 'no' only:\n")
	
		# increasing attempt by one
		count= count + 1
		
		# printing exiting message
		if count >= 5:
			print ("\n Non cooperative user. Exiting the game.\n")
			exit()
	
		# again asking for correct input
		play = raw_input("\n")

		# checking if user is interested in playing
	if play.lower() == 'no':
		print ("\nThanks for Playing. Have a nice day\n")


