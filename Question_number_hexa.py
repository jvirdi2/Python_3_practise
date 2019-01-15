# Helps in getting different types of representation of a decimal number.
# The output is as "decimal octet  hexadecimal binary"
def print_formatted(number):
    # your code goes here
    width = len(str(bin(number)))-2
    for num in range(1,number+1): 
        for base in 'doXb':
            print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
        print ('')



if __name__ == '__main__':
    n = 5
    print_formatted(n)
