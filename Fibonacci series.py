Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fib(n):
...     a = 0
...     b = 1
...     i = 0
...     if n <= 0:
...         print ('Input a positive number and try again')
...     elif n == 1:
...         print (a)
...     else:
...         print (a)
...         print (b)
...         for i in range (n-2):
...             c = a + b
...             print (c)
...             a = b
...             b = c
...             if i == (n-2):
...                 break
... 
...             
>>> def main():
...     fib(int(input('How many numbers do you need? ')))
... 
...     
>>> main()
How many numbers do you need? 5
0
1
1
2
3
