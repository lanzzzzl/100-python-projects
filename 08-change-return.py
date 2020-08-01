'''
Change Return Program - 
The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, 
dimes, nickels, pennies needed for the change.
'''

def change_return(cost,money_given):
    # quater = 0.25,dime = 0.1,nickel = 0.05 pennies = 0.01
    
    change = round(money_given-cost,2)
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while change >= 0.25:
        change -= 0.25
        quarters+=1
    while round(change,2) >= 0.1:
        change-= 0.1
        dimes +=1
    while round(change,2) >= 0.05:
        change-=0.05
        nickels +=1
    while round(change,2) > 0:
        change-=0.01
        pennies+=1
    return round(money_given-cost,2),quarters,dimes,nickels,pennies

change,quarters,dimes,nickels,pennies = change_return(1.45,2)
print(f'Your change is ${change}. {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s) and {pennies} pennie(s)')
