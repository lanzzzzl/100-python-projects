'''
Calculator - A simple calculator to do basic operators. 
Make it a scientific calculator for added complexity.
'''

def calculator(*args):
    
    op = args[-1]
    if op not in '+-*/':
        print("Only accepts + - * and /")
        return
    else:
        string = str(args[0])
        result = args[0]
        
    if op == '+':
        for i in range(1,len(args)-1):
            string += f' + {str(args[i])}'
            result += args[i]
        return f'{string} = {result}'
    elif op == '-':
        for i in range(1,len(args)-1):
            string += f' - {str(args[i])}'
            result -= args[i]
        return f'{string} = {result}'
    elif op == '*':
        for i in range(1,len(args)-1):
            string += f' * {str(args[i])}'
            result *= args[i]
        return f'{string} = {result}'
    elif op == '/':
        for i in range(1,len(args)-1):
            string += f' / {str(args[i])}'
            result /= args[i]
        return f'{string} = {result}'
    
calculator(1,2,3,'/')
# input a number of ints and an operator at last
