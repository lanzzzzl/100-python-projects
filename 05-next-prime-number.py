"""
Next Prime Number - 
Have the program find prime numbers until the user 
chooses to stop asking for the next one.
"""

def prime_num():
    print('First prime is 2\t')
    again = input('Would you like to know the next prime number? (y/n) ').lower()
    if again == 'y':
        pass
    elif again == 'n':
        return
    i = 3
    next_p = True
    while next_p:
        prime = True
        for num in range(3,i,2): # when i=3, this loop is not executed,fortunately 3 is a prime number. 
            if i % num == 0:
                prime = False
        if prime:
            print(f'\tNext prime is {i}')
            i+=2
            again = ''
            while again != 'y' and again!= 'n':
                again = input('\nWould you like to know the next prime number? (y/n) ').lower()
                if again == 'y':
                    next_p = True
                elif again == 'n':
                    next_p = False
                else:
                    print('y or n only please.')
        else:
            i+=2
            continue

if __name__ == "__main__":
	prime_num()