# Purchase tax calculator
# Configured just for Australia with a 10% purchase tax

def calcTax(cost, country='Australia'):

    countries = {'Australia' : 10}

    if country in countries.keys():
        tax = (cost / 100) * countries[country]
    else:
        return "Country can't be found"

    return tax

def main():

    tax = calcTax(int(input('What was the cost of your purchase? ')),
    input('Which country are you in? '))

    if type(tax) == str:
    	print(tax)
    else:
    	print('The tax on your purchase was:', tax)

    	
main()
