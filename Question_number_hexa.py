# Helps in getting different types of representation of a number as hexadecimal etc.
def print_formatted(number):
    # your code goes here
    width = len(str(bin(number)))-2
    for num in range(1,number+1): 
        for base in 'doXb':
            print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
        print ('')



if __name__ == '__main__':
    n = 2
    print_formatted(n)
