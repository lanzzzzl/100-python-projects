'''
Prime Factorization - 
Have the user enter a number and find all Prime Factors 
(if there are any) and display them.
'''

'''
function: prime_with_print(number) 
Returns a list of all prime factors,
and prints the calculations
'''
def prime_with_print(number):
    result = []
    threshold = number//2+1 # only necessary to iterate through the first half of numbers
    if number % 2 ==0:
        result.append(2)
    while number%2 == 0:
        print(f'2 is a divisor of {number}')
        number = number/2
        print(f'\tresulted in {number} ')

    for i in range(3,threshold,2):
        print(f'\nCurrently checking {i}')
        if number % i != 0:
            print(f'{i} is not a divisor of {number}')
            print(f'pass on {i+1}')
            continue
        
        while number % i == 0:
            print(f'\t{i} is a divisor of {number}')
            number = number / i
            print(f'\tresulted in {number}')
        result.append(i)
        if number == 1:
            break
        print(f'\npass on {i+1}')
        if i > number:
            break
    return result
    
    
'''
function: prime_set(number) 
Returns a list of all prime factors
'''
def prime_set(number): # using set to avoid duplicate values
    result = set()
    threshold = number // 2 + 1
    while number % 2 == 0:
        result.add(2)
        number = number / 2
    
    for i in range(3,threshold,2):  factor.
        while number % i == 0: # keep dividing the same number until not a divisor, to avoid adding a none prime
            result.add(i)
            number = number / i 
        else:
            continue
    return list(result)



'''
function: prime_list(number) 
Returns a list of all prime factors
'''
def prime_list(number): # using list, each factor only added once into the list
    result = []
    threshold = number // 2 + 1
    if number % 2 == 0:
        result.append(2)
    while number % 2 == 0:
        number = number / 2
    
    for i in range(3,threshold,2):
        if number % i == 0:
            result.append(i)
            while number % i == 0:
                number = number / i
        else:
            continue
    return result


if __name__ == "__main__":
    number = int(input("Enter a number to find all it's Prime Factors"))
    prime_with_print(number)
