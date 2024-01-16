# Calculator:
# - Last operation result value
# - New operand value
# - Operator

result = 0
operand = 0
operator = ''

while operator != 'x':

    print('\nCurrent: ', result)
    operator = input('Enter your operator (+,-,*,/) or \'x\' to Exit: ')
    if(operator=='x'):
        exit()
    
    operand  = float(input ('Enter operand: '))
    
    if(operator=='+'):
        result = result + operand
    if(operator=='-'):
        result = result - operand
    if(operator=='*'):
        result = result * operand
    if(operator=='/'):
        result = result / operand