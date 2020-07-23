'''
Find e to the Nth Digit - 
Just like the previous problem, but with e instead of π (pi). 
Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go.
'''

import math

def e_to_the_nth_digit():
	while True:
		try:
			n = int(input("How many digits of e? "
		except:
			print('Please enter a number between 1 and 15. ')
			continue
		if n > 15 or n < 0:
			print("The number you entered is out of range.")
		else:
			break

if __name__ == "__main__":
	e_to_the_nth_digit()
