def calculator(a, b, x):
        if x == '+':
            return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a + b))
        if x == '-':
            return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a - b))
        if x == '*':
            return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a * b))
        if x == '/':
            return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a / b))
        else:
            return 'Error please select an operator'
 
def main():
    a = int(input('Please type the first number: '))
    b = int(input('please type the second number: '))
    x = input('What operation would you like to carry out? \nChoose between "+,-,*,/": ')

    print (calculator(a, b, x))

    
main()
