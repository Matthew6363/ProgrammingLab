class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):

        self.name = name

        if (type(self.name) != str):
            
            raise ExamException ('errore generato da {}'.format(name))

    def get_data(self):

        my_list = []

        my_file = open(self.name, 'r')

        for line in my_file:

            riga = line.split(',')

            if riga [0] != 'date':
                
                riga[1] = riga[1][0:-1]
                
                my_list.append(riga)

        return my_list

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(time_series)



def detect_similar_monthly_variations(time_series, years):

    i = 0

    lista = []

    while i < 24:
        
        diff = time_series[i+1][1]-time_series[i][1]

        i = i+1

        lista.append(diff)

    return lista
l
print(lista)




