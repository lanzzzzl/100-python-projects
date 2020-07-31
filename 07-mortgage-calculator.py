import sys

def mortgage_calculator(rate,pv,n=1,interval='annually'):
    
    interval = interval.lower()
    
    terms = 0
    
    if interval == 'annually':
        terms = 1
    elif interval == 'quaterly':
        terms = 4
    elif interval == 'monthly':
        terms = 12
    elif interval == 'weekly':
        terms = 52
    elif interval == 'daily':
        terms = 365
    else:
        print('The interval you entered is invalid. (annually,quaterly,monthly,weekly or daily)')
        print('Default interval is annually.')
        terms = 1
    

    rate_per_period = rate / terms
    present_value = pv
    num_of_terms = n * terms
    
    pmt = (rate_per_period * present_value) / (1 - (1 + rate_per_period)**(-num_of_terms))
    print(pmt)

    return pmt

'''
usage: mortgage_calculator(anual_interest_rate, total_mortgage, num_of_years,*interval = annually)
'''

if __name__ == "__main__":
    print(sys.argv)

    rate,pv,n,interval = sys.argv[1:]
    mortgage_calculator(float(rate),float(pv),int(n),interval)
