# Questo file legge ripa per riga ognuno dei file e crea un
# file per ogni squadra e mette una statistica per riga.
# Inoltre per ogni squadra memorizzo quale sarà il prossimo match

import glob
import os

class squad:
    def prova(self):
        Lsquad=[]
        currentline=""
        with open('squad.json', 'r') as f:
            for line in f:
                currentline = line.split(",")
            f.close()
            i=40
            j=0
        with open('squad.json', 'w') as f:
            while i<60:
                Lsquad.insert(j,currentline[i])
                f.write(currentline[i].replace("[","").replace("]","").replace("'","")+'\n')
                i=i+1
                j=j+1


        for file_name in glob.iglob('C:\\Users\\gsavi\\root\\Giuseppe\\Progetti\\SerieA\\*.json', recursive=True):
            with open(file_name, 'r') as f:
                    line = f.readlines()
                    j=0
                    while j<20:
                        i=0
                        a0=line.__len__()
                        while i<(a0-2):
                            prova= line[i].split()
                            if prova[0].__contains__(Lsquad[j]) or prova[1].__contains__(Lsquad[j]) or prova[2].__contains__(Lsquad[j]) or prova[3].__contains__(Lsquad[j]) or prova[4].__contains__(Lsquad[j])  or prova[5].__contains__(Lsquad[j])  or prova[6].__contains__(Lsquad[j]) :
                                with open("Squadre/" + Lsquad[j] + ".txt", 'a') as file:
                                    file.write( line[i])
                                file.close()
                            i=i+1
                        j=j+1

