
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
                
                if all('' == s or s.isspace() for s in riga[1]):

                    riga[1] = 0

                try:

                    riga[1] = int (riga[1])

                except : 

                    riga[1] = 0


                else:

                    riga[1] = riga[1]

                my_list.append(riga)

                time_stamp.append(riga[0][:4])

        for x in range (len(my_list)-1):
            for h in range (x+1,len(my_list)):
                if my_list[x][0] == my_list[h][0]:
                    raise ExamException ('Ci sono dati duplicati nel file')

        for x in range(len(time_stamp)-1):
            if time_stamp[x+1] < time_stamp[x]:
                raise ExamException('Sequenza temporale non ordinata')


        return my_list

mesi = ["01","02","03","04","05","06","07","08","09","10","11","12"]
anno = {"01":30, "03":107}

def sistema_tutto_che_se_no_mi_arrabbio(mesi, anno):
    ''' 'La funzione prende in argomento una lista per avere i mesi come chiave e un dizionario in cui inserire chiavi. Se non sono presenti, alza un errore. Se lo alza, metto 0.
        1Se non alza un errore invece, metto in da_ritornare la chiave "mesi[i]" e ci associ il valore che c'è nella corrispondente di anno.'''
        
    
    lista = []
    da_ritornare = dict() #dizionario vuoto, {}
    for i in range(12): #i lo uso come iteratore per tutto il processo
        try: #chiamare una chiave che non esiste alza un KeyError. Metto un try.
            da_ritornare[mesi[i]] = anno[mesi[i]] 
            lista.append(anno[mesi[i]])
        except: #Non ho quella chiave
            #Devo mettere 0 in chiave che manca
            da_ritornare[mesi[i]] = 0
            lista.append(0)
            
    return lista



def detect_similar_monthly_variations(time_series, years):

    #controllo che la lista years non sia vuota
    if not years:
        raise ExamException('Errore : la lista degli anni è vuota')
    #controllo che la lista abbia il giusto numero di elementi
    if len(years) > 2 or len(years) < 2:
        raise ExamException('Errore: la lista degli anni fornita non ha il numero corretto di elementi')

    # controllo che time_series sia una lista
    if not isinstance(time_series, list):
        raise ExamException('Errore: time_series non è una lista di liste')

    # Controllo che tutti gli anni siano numero interi:
    if not isinstance(years[0], int) or not isinstance(years[1], int):
        raise ExamException('Errore gli anni forniti non sono numeri interi')

    #controllo che i due anni forniti siano differenti

    if years[0] == years[1]:
        raise ExamException('Errore: i due anni devono essere diversi ! ')

    # Il primo anno deve essere piu piccolo del secondo
    if years[0] > years[1]:
        tmp = years[0]
        years[0] = years[1]
        years[1] = tmp

    # Controllo che il primo anno sia presente nella lista time_series
    if years[0] < int(time_series[0][0][:4]):
        raise ExamException('Errore: il primo anno non è presente nella lista')
    #controllo che il secondo anno sia presente nella lista time_series
    if years[1] > int(time_series[-1][0][:4]):
        raise ExamException('Errore: l\' anno finale non è presente nella lista ! ')

    # Controllo che gli anni siano consecutivi
    if years[1] != years[0] + 1:
        raise ExamException('Errore: gli anni non sono consecutivi ')


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

        diff = lista_variaz_primo_anno[i] - lista_variaz_sec_anno[i]

        if diff == lista_variaz_primo_anno[i] or diff == lista_variaz_sec_anno[i]:
            diff = 4

        if(diff > 2 or diff < -2 ):
            lista_finale.append(2<1)

        else: lista_finale.append(1<2)

    return lista_finale

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
years = [1949,1950]
print(detect_similar_monthly_variations(time_series, years))

   



