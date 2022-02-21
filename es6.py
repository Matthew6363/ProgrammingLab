
class ExamException:
    pass



class CSVTimeSeriesFile():
    def __init__(self, name):

        self.name = name

        if (type(self.name) != str):

            print('Nome file non è una stringa')

            try:

                self.name = str(name)

            except Exception:

                raise ExamException ('Non è stato possibile effettuare la conversione')
                
    def get_data(self):

        my_list = []

        time_stamp = []

        try: 

            my_file = open(self.name, 'r')

          

        except Exception :

            raise ExamException ("Non è possibile aprire il file")
            
            my_file.close()

        
            
        for line in my_file:

            riga = line.split(',')

            if riga [0] != 'date':
                
                riga[1] = riga[1][0:-1]
                
                my_list.append(riga)

                time_stamp.append(riga[0])

        for x in range (len(my_list)-1):
            for h in range (x+1,len(my_list)):
                if my_list[x][0] == my_list[h][0]:
                    raise ExamException ('Ci sono dati duplicati nel file') 

        for x in range(len(time_stamp)-1):
            if time_stamp[x+1] < time_stamp[x]:
                raise ExamException('Sequenza temporale non ordinata')


        return my_list



def detect_similar_monthly_variations(time_series, years):

    
    if years[0] not in time_series[] or years [1] not in time_series: 
        
        raise ExamException ('Almeno uno dei due anni non è presente nel file')

    if years[1] != years[0]+1:
        raise ExamException ('anni non successivi')

   


    lista_variaz_primo_anno = []
    lista_variaz_sec_anno = []
    lista_finale = []
    
    pass_primo_anno = [riga[1] for riga in time_series if riga[0][0:4] == str(years[0])]
    
    
    pass_sec_anno = [riga[1] for riga in time_series if riga[0][0:4] == str(years[1])]
  

    for i in range(12):
        pass_primo_anno[i] = int (pass_primo_anno[i])
        pass_sec_anno[i] = int (pass_sec_anno[i])

    for i in range(11):
        variaz_mesi_primo_anno = pass_primo_anno[i+1]-pass_primo_anno[i]

        variaz_mesi_sec_anno = pass_sec_anno[i+1]-pass_sec_anno[i]  

        lista_variaz_primo_anno.append(variaz_mesi_primo_anno)

        lista_variaz_sec_anno.append(variaz_mesi_sec_anno)

        if(lista_variaz_primo_anno[i] - lista_variaz_sec_anno[i] > 2 or lista_variaz_primo_anno[i] - lista_variaz_sec_anno[i] < -2 ):
            lista_finale.append(2<1)

        else: lista_finale.append(1<2)

    return lista_finale

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
years = [1958,1953]
print(time_series)
print(detect_similar_monthly_variations(time_series, years))


