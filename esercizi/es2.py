my_values = []

my_file = open('shampoo_sales.csv','r')
for line in my_file:

    el = line.split(',')

    if el[0] != 'Date':

        date =  el[0]
        val = el [1]

        my_values.append(float(val))

print('{}' .format(sum(my_values)))


