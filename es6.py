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

#time_series_file = CSVTimeSeriesFile(name='data.csv')
#time_series = time_series_file.get_data()



def detect_similar_monthly_variations(time_series, years):

    ci = []
    di = []
    lista_fin = []
    
    a = [riga[1] for riga in time_series if riga[0][0:4] == str(years[0])]
    
    
    b = [riga[1] for riga in time_series if riga[0][0:4] == str(years[1])]
  

    for i in range(12):
        a[i] = int (a[i])
        b[i] = int (b[i])

    for i in range(11):
        c = a[i+1]-a[i]
        d = b[i+1]-b[i]  
        ci.append(c)
        di.append(d)
        if(ci[i] - di[i] > 2 or ci[i] - di[i] < -2 ):
            lista_fin.append('False')

        else: lista_fin.append('True')

    return lista_fin

#for i in range(11):
    
    years = [1949+i,1949+i+1]
    print(detect_similar_monthly_variations(time_series, years))

