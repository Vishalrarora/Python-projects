Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculator(a, b, x):
...         if x == '+':
...              return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a + b))
...         if x == '-':
...             return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a - b))
...         if x == '*':
...             return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a * b))
...         if x == '/':
...             return(str(a) + ' ' + x + ' ' + str(b) + ' = ' + str(a / b))
...         else:
...             return 'Error please select an operator'
... 
... 
>>> def main():
...     a = int(input('Please type the first number: '))
...     b = int(input('please type the second number: '))
...     x = input('What operation would you like to carry out? \nChoose between "+,-,*,/": ')
... 
...     print (calculator(a, b, x))
... 
...     
>>> main()
Please type the first number: 8
please type the second number: 9
What operation would you like to carry out? 
Choose between "+,-,*,/": -
8 - 9 = -1
