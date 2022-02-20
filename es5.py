class error(Exception):
    pass

class CSVfile():
    
    def __init__(self,name):

        self.name = name

        if type(self.name) != str:

            raise error('Il nome del file non è una stringa')

        try: 

            my_file = open(self.name, 'r')

        except Exception as e:

            print("Non è possibile aprire il file")

    def get_data(self,start, end):

        self.start = start

        self.end = end

        if(start > end) :
            
            tmp = start
            start = end
            end = tmp
        

        my_list = [] 

        my_file = open(self.name,'r')

        i = 0

        for line in my_file:

            i +=1

            riga = line.split(',')
         
            if riga[0] != 'Date':
               
                riga[1] = riga[1][0:-1]
                
                if i > start and i < end:

                    my_list.append(riga)

        return my_list

class NumericalCSVfile(CSVfile):
  
    def conv(self):
       
        my_list = super().get_data()

        for riga in my_list:
           
            for i, item in enumerate (riga):
           
                if(i != 0):
                    try:
                        riga[i] = float(item)
                    except ValueError:
                        print('Errore di conversione, elemento = {} non convertibile '.format(item))
                        riga[i] = 0.0
    
        return my_list

file1 = NumericalCSVfile('shampoo_sales.csv')
print(file1.get_data(20,10))


