import datetime

class ExamException(Exception):
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

             
                
                if all('' == s or s.isspace() for s in                  riga[1]):

                       riga[1] = 0

                try:
                    
                    riga[1] = int (riga[1])

                except : 

                    riga[1] = 0

                if riga[1] <0:
                    riga[1] = -riga[1]
                
                try:
                    datetime.datetime.strptime(riga[0], '%Y-%m')
                except:
                    raise ExamException ('date non corrette')
                 
                my_list.append(riga)

                time_stamp.append(riga[0])

        if not my_list:
            raise ExamException('Lista non completa')

    

        for x in range (len(my_list)-1):
            for h in range (x+1,len(my_list)):
                if my_list[x][0] == my_list[h][0]:
                    raise ExamException ('Ci sono dati                      duplicati nel file')

        for x in range(len(time_stamp)-1):
            if time_stamp[x+1] < time_stamp[x]:
                raise ExamException('Sequenza temporale                 non ordinata')

     



        return my_list




def detect_similar_monthly_variations(time_series, years):

    #controllo che la lista years non sia vuota
    if not years:
        raise ExamException('Errore : la lista degli            anni è vuota')
    #controllo che la lista abbia il giusto numero di       elementi
    if len(years) > 2 or len(years) < 2:
        raise ExamException('la lista degli             anni fornita non ha il numero corretto di               elementi')

    # controllo che time_series sia una lista
    if not isinstance(time_series, list):
        raise ExamException('time_series non è          una lista di liste')

    # Controllo che tutti gli anni siano numero interi:
    if not isinstance(years[0], int) or not isinstance(years[1], int):
        raise ExamException('gli anni forniti non sono numeri interi')

    #controllo che i due anni forniti siano differenti

    if years[0] == years[1]:
        raise ExamException('i due anni forniti devono essere diversi ! ')

    # Il primo anno deve essere piu piccolo del secondo, in caso negativo scambio gli anni forniti
    if years[0] > years[1]:
        tmp = years[0]
        years[0] = years[1]
        years[1] = tmp

    # Controllo che il primo anno sia presente nella lista time_series
    if years[0] < int(time_series[0][0][:4]):
        raise ExamException('il primo anno non è presente nella lista')
    #controllo che il secondo anno sia presente nella lista time_series
    if years[1] > int(time_series[-1][0][:4]):
        raise ExamException('l\' anno finale non è presente nella lista ! ')

    # Controllo che gli anni siano consecutivi
    if years[1] != years[0] + 1:
        raise ExamException('gli anni non sono consecutivi ')

    #creo tre liste vuote rispettivamente per, salvare le variazioni mensili tra mesi consecutivi del primo anno, .... del secondo anno e infine creare la lista contenente i True e False a richiesta
    lista_variaz_primo_anno = []
    lista_variaz_sec_anno = []
    lista_finale = []

    #con una lista comprehension riempio due liste con i dati riguardanti il numero mensile di passeggeri 

    pass_primo_anno = [riga[1] for riga in time_series if riga[0][0:4] == str(years[0])]

    pass_sec_anno = [riga[1] for riga in time_series if riga[0][0:4] == str(years[1])]

   #calcolo le variazioni del num dei pass per per il primo e il secondo anno forniti e li inserisco nelle apposite liste

    c = len(pass_primo_anno)-1

    d = len(pass_sec_anno)-1

    for i in range(c):
        
        variaz_mesi_primo_anno = pass_primo_anno[i+1]-pass_primo_anno[i]

        lista_variaz_primo_anno.append(variaz_mesi_primo_anno)

    for h in range(c):

        variaz_mesi_sec_anno = pass_sec_anno[h+1]-pass_sec_anno[i]

        

        lista_variaz_sec_anno.append(variaz_mesi_sec_anno)

        #verifico la similitudine tra le variazioni di mesi successivi e la pongo falsa se una delle due variazioni è invariata, riempio una lista con i True e False a seconda del caso

    if c == d:

        for i in range(d):
        
            diff = lista_variaz_primo_anno[i] - lista_variaz_sec_anno[i]

            

            if(diff > 2 or diff < -2 ):
                lista_finale.append(2<1)

            else: lista_finale.append(1<2)

    return lista_finale


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()



years = [1950,1951]

print(detect_similar_monthly_variations(time_series, years))