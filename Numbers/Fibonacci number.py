# Enter a number and return the corresponding value in the fibonacci series

def fib(x):
    assert isinstance(x, int) and x >= 0

    n_1, n_2, i = 0, 1, 2

    if x == 0:
        return n_1
    elif x == 1:
        return n_2
    else:
        while i < x:
            n_new = n_1 + n_2
            n_1, n_2 = n_2, n_new
            i += 1
    return n_2

def main():

    x = int(input('Enter a number to get its corresponding fibonacci value: '))
    print('The fibonacci value ', x, 'is:', fib(x))

main()
