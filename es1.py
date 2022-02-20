def sum_list(my_list):

    somma = 0

    for item in my_list:

        somma = somma + item

    return somma

my_list = [1,2,3,4,5]
somma = sum_list(my_list)
print('somma = {} ' .format(somma))

