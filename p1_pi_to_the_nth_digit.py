'''
Find PI to the Nth Digit - 
Enter a number and have the program generate π (pi) 
up to that many decimal places. 
Keep a limit to how far the program will go.
'''

import math

def pi_to_the_nth_digit():
	while True:
		try:
			n = int(input('How many digits of PI? (Up to 15 only)'))
		except:
			print('Please enter a number between 1 and 15. '
			continue
		if n<1 or n > 15:
			print('The number you entered is out of bound. Please try again. ')
		else:
			break

if __name__ == "__main__":
	pi_to_the_nth_digit()