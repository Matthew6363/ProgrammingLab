class CSVfile():
    def __init__(self, name):

        self.name = name
        
    def get_data(self):

        my_list = []

        my_file = open(self.name, 'r')

        for line in my_file:

            riga = line.split(',')

            if riga [0] != 'Date':
                
                riga[1] = riga[1][0:-1]
                
                my_list.append(riga)

              
        return my_list

file1 = CSVfile('shampoo_sales.csv')
print('Lista: {}'.format(file1.get_data()))