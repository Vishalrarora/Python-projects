def fib(n):
    a = 0
    b = 1
    i = 0
    if n <= 0:
        print ('Input a positive number and try again')
    elif n == 1:
        print (a)
    else:
        print (a)
        print (b)
        for i in range (n-2):
            c = a + b
            print (c)
            a = b
            b = c
            if i == (n-2):
                break
             
def main():
    fib(int(input('How many numbers do you need? ')))

main()
