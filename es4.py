class CSVfile():
    #funzione per inizializzare la classe, da fare sempre
    def __init__(self,name):

        self.name = name
    #gestisco eventuali errori nell'apertura dei file
        try: 

            my_file = open(self.name, 'r')

        except Exception as e:

            print("Non è possibile aprire il file")
    #definisco la funzione get_data, creerà una lista di liste
    def get_data(self):

        my_list = [] #lista vuota dove salvare i valori
        #apro in lettura il file 
        my_file = open(self.name,'r')
        #controllo linea per linea, spezzandola all'atezza della virgola, per ogni virgola presente 
        for line in my_file:

            riga = line.split(',')
            #salto la prima riga del file perchè formata da stringhe e non di mio interesse. ovvero controllo se la riga inizia o no con Date ed eventualmente la salto
            if riga[0] != 'Date':
                #escludo l'ultimo carattere della riga(\n)
                
                riga[1] = riga[1]
                #aggiungo alla mia lista vuota gli elementi creati
                my_list.append(riga)

        return my_list

class NumericalCSVfile(CSVfile):
    #creo una funzione che converta a numero tutti gli elementi tranne quelli della prima colonna (col indice 0)
    def conv(self):
        #richiamo il metodo get_data dalla classe padre, che mi fornisce la lista su cui iterare
        my_list = super().get_data()

        for riga in my_list:
            #numero gli elementi della riga (quelli splittati dalla virgola)
            for i, item in enumerate (riga):
                #se l'indice dell'elemento è diverso da 0 ed è convertibile, lo converto a numero float. Uso il costrutto try-except per la gestione dei casi imprevisti, ovvero elementi non convertibili a numero. Il costrutto darà un valore standard di 0.0 come risultato della conversione dei casi imprevisti e stamperà una stringa che indica l'elemento generante l'errore
                if(i != 0):
                    try:
                        riga[i] = float(item)
                    except ValueError:
                        print('Errore di conversione, elemento = {} non convertibile '.format(item))
                        riga[i] = 0.0
        #ritorno la lista contenente i valori convertiti a numero
        return my_list

file1 = NumericalCSVfile('shampoo_sales.csv')
print(file1.conv())


