from bs4 import BeautifulSoup
import requests


def funzionedicazzo(a):
        for prova in a:
            if(str(prova).__contains__(':')):
                return False
        return True


class Scrapy1:


    def estrpolaOut(self):
        html = requests.get('https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate').text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('tr', class_='odd', height=28)

        dcount = 0
        data = []
        m=""

        with open('calendar.json', 'w') as f:
            for tag in tags:
                word = tag.text.split()
                if ((len(word) > 5) and funzionedicazzo(word)):
                    word.pop(1)
                    word.pop(0)
                    a = word[len(word) - 1]
                    b = a.split('stats')
                    word.pop(len(word) - 1)
                    if (len(b) == 2):
                        g1 = b[1].split(')')
                        m1 = g1[0].split('(')
                    word.append(b[0])
                    word.append(m1[1])
                    c = list(word[0])
                    c.pop(2)
                    c.pop(1)
                    c.pop(0)
                    word.pop(0)
                    d = ''.join(c)
                    word.insert(0, d)
                    dcount = dcount + 1
                    dc = str(dcount)
                    if len(word) == 6:
                        m= "Match: "+  dc +" Squadre: "+  word[0]+  " "+ word[len(word) - 2] + " Risultato: "+ word[1] + word[2] + word[3]+ " Parziale: "+ word[len(word) - 1]
                        m = str(m) + '\n'
                        data.append(m)



                    if len(word) == 8:
                        m = "Match: " +dc+ " Squadre: "+ word[0] + word[1]+ ":"+ word[len(word) - 3] + word[len(word) - 2]+ " Risultato: "+ word[2] + word[3] + word[4]+" Parziale: "+ word[len(word) - 1]
                        m = str(m) + '\n'
                        data.append(m)


                    if (len(word) == 7) and (len(word[1]) > 1):
                        m = "Match: " +dc+" Squadre: " + word[0] + word[1]+" "+ word[len(word) - 2]+" Risultato: "+ word[2] + word[3] + word[4]+" Parziale: "+ word[len(word) - 1]+ '\n'
                        data.append(m)


                    if (len(word) == 7) and (len(word[len(word) - 3]) > 1):
                        m = "Match: "+ dc + " Squadre: " +  word[0] +" "+ word[len(word) - 3] + word[len(word) - 2]+ " Risultato: "+ word[1] + word[2] + word[3]+" Parziale: "+ word[len(word) - 1]+'\n'

                        data.append(m)

                    num=len(m)



            with open('calendar.json', 'w') as f:
                        for prova in data:
                            f.write(str(prova))

    def estrpolaClassifica(self):

        def foo(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return 0

        html1 = requests.get('https://www.soccerstats.com/widetable.asp?league=italy').text
        soup1 = BeautifulSoup(html1, 'html.parser')
        tags = soup1.find_all('tr', class_='odd')
        a = []
        data = []
        m = {}

        for tag in tags:
            a = tag.text.split('\n')
            a.pop(len(a) - 1)
            a.pop(len(a) - 6)
            a.pop(len(a) - 6)
            a.pop(len(a) - 6)
            a.pop(len(a) - 6)
            a.pop(len(a) - 11)
            a.pop(len(a) - 12)
            b = a[2].split('\xa0')
            b.pop(0)
            b.pop(1)
            a.pop(0)
            a.pop(1)
            a.insert(1, b)
            a[1] = ''.join(a[1])

            m = {
                "Posizione": str(a[0])+": " + str(a[1]),
                "Partite Giocate": int(a[2]),
                "Vittorie": int(a[3]),
                "Pareggi": int(a[4]),
                "Sconfitte": int(a[5]),
                "Gol Fatti":int(a[6]),
                "Gol Subiti": int(a[7]),
                "Differenza Reti": int(a[8]),
                "Punti": int(a[9]),
                "Punti per Partita": float(a[10]),
                "Goal a partita": (int(a[6]) / int(a[2])),
                "Vittorie in casa": a[11],
                "Pareggi in casa": a[12],
                "Sconfitte Casa": a[13],
                "Goal In Casa": a[14],
                "Goal Per Match In casa": str(foo(int(a[14]), (int(a[11]) + int(a[12]) + int(a[13])))),
                "Goal Subiti In casa": a[15],
                "Goal Subiti Per match in casa": str(foo(int(a[15]), (int(a[11]) + int(a[12]) + int(a[13])))),
                "Vittorie Trasferta": a[16],
                "Pareggi Trasferta": a[17],
                "Sconfitte In Trasferta": a[18],
                "Goal in Trasferta": a[19],
                "Goal Per Match In trasferta": str(foo(int(a[19]), (int(a[18]) + int(a[17]) + int(a[16])))),
                "Goal Subiti in Trasferta": a[20],
                "Goal Subiti per Match in Trasferta": str(foo(int(a[20]), (int(a[18]) + int(a[17]) + int(a[16]))))+"\n"
            }
            if len(a) == 16:
                m = {
                    "Posizione": str(a[0]) +": "+ str(a[1]),
                    "Partite Giocate": a[2],
                    "Vittorie": a[3],
                    "Pareggi": a[4],
                    "Sconfitte": a[5],
                    "Gol Fatti": a[6],
                    "Gol Subiti": a[7],
                    "Differenza Reti": a[8],
                    "Punti": a[9],
                    "Punti per Partita": a[10],
                    "Goal a partita": (int(a[7]) / int(a[3])),
                    "Vittorie in casa": a[11],
                    "Pareggi in casa": a[12],
                    "Sconfitte Casa": a[13],
                    "Goal In Casa": a[14],
                    "Goal Per Match In casa": str(int(a[14]) / (int(a[11]) + int(a[12]) + int(a[13]))),
                    "Goal Subiti In casa": a[15],
                    "Goal Subiti Per match in casa": str(int(a[15]) / (int(a[11]) + int(a[12]) + int(a[13]))),
                    "Vittorie Trasferta": a[16],
                    "Pareggi Trasferta": a[17],
                    "Sconfitte In Trasferta": a[18],
                    "Goal in Trasferta": a[19],
                    "Goal Per Match In trasferta": str(int(a[19]) / (int(a[18]) + int(a[17]) + int(a[16]))),
                    "Goal Subiti in Trasferta": a[20],
                    "Goal Subiti per Match in Trasferta": str(
                        int(a[20]) / (int(a[18]) + int(a[17]) + int(a[16])))

                }

            data.append(str(m)+'\n')

        with open('classifica.json', 'w') as f:
                for prova in data:
                    f.write(str(prova))

    def estrpolaNO_GOAL(self):
        html = requests.get('https://www.soccerstats.com/table.asp?league=italy&tid=z').text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('tr', class_='odd')

        data = []
        m = {}
        ind = 0

        for tag in tags:
            if ind<20:
                a = tag.text.split()
                if len(a) == 4:
                    m = {"squadra": str(a[0]),
                     "failed to score": a[1],
                     "matches played": a[2],
                     "percentuale": a[3]
                     }


                if len(a) == 5:
                    m = {"squadra": str(a[0] + a[1]),
                     "failed to score": a[2],
                     "matches played": a[3],
                     "percentuale": a[4]
                     }
                data.append(str(m)+"\n")
            ind=ind+1
        with open('NO_GOAL.json', 'w') as f:
                for prova in data:
                    f.write(str(prova))


    def estrpolaMarcatori(self):
        html = requests.get('https://www.soccerstats.com/scorers.asp?league=italy').text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('tr', class_='odd')

        data = []
        m = {}
        for tag in tags:
            a = tag.text.split()
            if (len(a) == 14) :
                m = {
                    "player": (a[0]),
                    "club": (a[1]),
                    "goals": a[2],
                    "home": a[3],
                    "away": a[4],
                    "goal 0,15": a[5],
                    "goal 0,30": a[6],
                    "goal 0,45": a[7],
                    "goal 0,60": a[8],
                    "goal 0,75": a[9],
                    "goal 1,90": a[10],
                    "last": a[11]+a[12],
                    "%team": a[13]
                }
            if (len(a) == 15) and (str(a[0]).__contains__(".")):
                m = {
                    "player": str(a[0])+str(a[1]),
                    "club": str(a[2]),
                    "goals": a[3],
                    "home": a[4],
                    "away": a[5],
                    "goal 0,15": a[6],
                    "goal 0,30": a[7],
                    "goal 0,45": a[8],
                    "goal 0,60": a[9],
                    "goal 0,75": a[10],
                    "goal 1,90": a[11],
                    "last": a[12]+a[13],
                    "%team": a[14]
                }

            if (len(a) == 15) and not(str(a[0]).__contains__(".")):
                m = {
                    "player": str(a[0]),
                    "club": str(a[1]+a[2]),
                    "goals": a[3],
                    "home": a[4],
                    "away": a[5],
                    "goal 0,15": a[6],
                    "goal 0,30": a[7],
                    "goal 0,45": a[8],
                    "goal 0,60": a[9],
                    "goal 0,75": a[10],
                    "goal 1,90": a[11],
                    "last": a[12]+a[13],
                    "%team": a[14]
                }
            if len(a) == 16:
                m = {
                    "player": str(a[0] + a[1]),
                    "club": str(a[2]+a[3]),
                    "goals": a[4],
                    "home": a[5],
                    "away": a[6],
                    "goal 0,15": a[7],
                    "goal 0,30": a[8],
                    "goal 0,45": a[9],
                    "goal 0,60": a[10],
                    "goal 0,75": a[11],
                    "goal 0,90": a[12],
                    "last": a[13]+a[14],
                    "%team": a[15]
                }
            data.append(str(m)+'\n')

        with open('marcatori.json', 'w') as f:
            for prova in data:
                f.write(str(prova))

    def estrpolaUNDER_OVER(self):
        html = requests.get('https://www.soccerstats.com/table.asp?league=italy&tid=c').text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('tr', class_='odd')

        data = []
        m = {}
        i=0
        for tag in tags:
            if i==61:
                break
            i=i+1
            a = tag.text.split()
            if len(a) == 14:
                m = {"matches of squadre": str(a[0]),
                     "matches played": a[1],
                     "average match goal": a[2],
                     "0.5": a[3],
                     "1.5+": a[4],
                     "2.5+": a[5],
                     "3.5": a[6],
                     "4.5": a[7],
                     "5.5": a[8],
                     "both teams scored": a[9],
                     "clean sheet": a[10],
                     "failed to score": a[11],
                     "Vittoria + Nogoal": a[12],
                     }
            if len(a) == 15:
                m = {"matches of squadre": str(a[0] + a[1]),
                     "matches played": a[2],
                     "average match goal": a[3],
                     "0.5": a[4],
                     "1.5+": a[5],
                     "2.5+": a[6],
                     "3.5": a[7],
                     "4.5": a[8],
                     "5.5": a[9],
                     "both teams scored": a[10],
                     "clean sheet": a[11],
                     "failed to score": a[12],
                     "Vittoria + Nogoal": a[13],
                     }
            if i==21:
                data.append("Match in casa:  ")
            if i == 41:
                data.append("Match in trasferta:  ")

            data.append(str(m)+'\n')
            with open('UNDER_OVER.json', 'w') as f:
                for prova in data:
                    f.write(str(prova))

    def estrpolaPasses(self):
        html = requests.get('https://fbref.com/en/comps/11/passing/Serie-A-Stats').text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('td')
        tags1 = soup.find_all('th')
        data=[]
        data1=[]
        ind=0
        p=["Giocatori impiegati","Passaggi completati", "Passaggi tentati", "Percentuale", "Distanza", "Distanza passaggi verso porta",
           "Passaggi corti completati " , "Passaggi corti tentati" , "Percentuale passaggi corti",
           "Passaggi medi completati", "Passaggi medi tentati", "Percentuale passaggi medi",
           "Passaggi lunghi completati", "Passaggi lunghi tentati", "Percentuale passaggi corti",
           "Passaggi che portano tiro","Passaggi completati last 30m campo","Passaggi completati in area avversaria", "Cross completati in area"
           ]
        for tag in tags:
                a = tag.text.split()
                data.append(a)
        while (ind < 480):
            data.pop(480)
            ind=ind+1
        ind =0
        num=0
        for tag1 in tags1:
            a=tag1.text.split()
            data1.append(a)
            ind=ind+1
            if ((ind>32) and (ind<53)):

                data.insert(num, str(a).replace("[","").replace("]"," ").replace("'",""))
                num=num+25
        i=499
        while (i>0):
            data.pop(i)
            data.pop(i-5)
            data.pop(i-6)
            data.pop(i-7)
            data.pop(i-22)
            i=i-25
        i=0
        ind=0
        while ((i<400)):

            data[i+1]=p[ind]+" "+str(data[i+1]).replace("[","").replace("]","")
            data[i+2]=p[ind+1]+" "+str(data[i+2]).replace("[","").replace("]","")
            data[i + 3] = p[ind+2] + " " + str(data[i + 3]).replace("[","").replace("]","")
            data[i + 4] = p[ind + 3] + " " + str(data[i + 4]).replace("[","").replace("]","")
            data[i + 5] = p[ind+4] + " " + str(data[i + 5]).replace("[","").replace("]","")
            data[i + 6] = p[ind + 5] + " " + str(data[i + 6]).replace("[","").replace("]","")
            data[i + 7] = p[ind+6] + " " + str(data[i + 7]).replace("[","").replace("]","")
            data[i + 8] = p[ind + 7] + " " + str(data[i + 8]).replace("[","").replace("]","")
            data[i + 9] = p[ind + 8] + " " + str(data[i + 9]).replace("[","").replace("]","")
            data[i + 10] = p[ind + 9] + " " + str(data[i + 10]).replace("[","").replace("]","")
            data[i + 11] = p[ind + 10] + " " + str(data[i + 11]).replace("[","").replace("]","")
            data[i + 12] = p[ind + 11] + " " + str(data[i + 12]).replace("[","").replace("]","")
            data[i + 13] = p[ind + 12] + " " + str(data[i + 13]).replace("[","").replace("]","")
            data[i + 14] = p[ind + 13] + " " + str(data[i + 14]).replace("[","").replace("]","")
            data[i + 15] = p[ind + 14] + " " + str(data[i + 15]).replace("[","").replace("]","")
            data[i + 16] = p[ind + 15] + " " + str(data[i + 16]).replace("[","").replace("]","")
            data[i + 17] = p[ind + 16] + " " + str(data[i + 17]).replace("[","").replace("]","")
            data[i + 18] = p[ind + 17] + " " + str(data[i + 18]).replace("[","").replace("]","")
            data[i + 19] = p[ind + 18] + " " + str(data[i + 19]).replace("[","").replace("]","") +"\n"

            i=i+20
            ind=0

        with open('PASStats.json', 'w') as f:
            for prova in data:
                f.write(str(prova))



    def estrpolaShot(self):
            html = requests.get('https://fbref.com/en/comps/11/shooting/Serie-A-Stats').text
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.find_all('td')
            tags1 = soup.find_all('th')
            data=[]
            data1=[]
            ind=0
            num=0
            i=0
            p = ["Goal", "Tiri", "TiriPorta", "Percentuale",
                 "TiriXPartita", "TiriPorta X partita ", "Goal Per tiri", "Goal  per tiri in porta",
                 "Distanza media  goal", "Punizioni calciate", "Rigori",
                 "Rigori segnati"
                 ]
            for tag in tags:
                a = tag.text.split()
                data.append(a)
                i=i+1
                if i>380:
                    data.pop(380)
            for tag1 in tags1:
                a = tag1.text.split()
                data1.append(a)
                ind = ind + 1
                if ((ind > 24) and (ind < 45)):

                    data.insert(num, str(a).replace("[","").replace("]"," ").replace("'",""))
                    num = num + 20
            i =399
            while (i > 0):
                data.pop(i)
                data.pop(i -1)
                data.pop(i - 2)
                data.pop(i - 3)
                data.pop(i - 4)
                data.pop(i-17)
                data.pop(i-18)
                i = i - 20
            i = 0
            ind = 0
            while ((i < 260)):
                data[i]=data[i]+"\t"
                data[i + 1] = p[ind] + " " + str(data[i + 1]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 2] = p[ind + 1] + " " + str(data[i + 2]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 3] = p[ind + 2] + " " + str(data[i + 3]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 4] = p[ind + 3] + " " + str(data[i + 4]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 5] = p[ind + 4] + " " + str(data[i + 5]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 6] = p[ind + 5] + " " + str(data[i + 6]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 7] = p[ind + 6] + " " + str(data[i + 7]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 8] = p[ind + 7] + " " + str(data[i + 8]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 9] = p[ind + 8] + " " + str(data[i + 9]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 10] = p[ind + 9] + " " + str(data[i + 10]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 11] = p[ind + 10] + " " + str(data[i + 11]).replace("[", "").replace("]", "").replace("'","")+"\t"
                data[i + 12] = p[ind + 11] + " " + str(data[i + 12]).replace("[", "").replace("]", "").replace("'","")+'\n'

                i = i + 13
                ind = 0
            with open('SHOTstats.json', 'w') as f:
                for prova in data:
                    f.write(str(prova))



    def estrpolaDefense(self):
            html = requests.get('https://fbref.com/en/comps/11/defense/Serie-A-Stats').text
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.find_all('td')
            tags1 = soup.find_all('th')
            data=[]
            data1=[]
            ind=0
            num=0
            i=0
            p = ["Tackle", "Tackle Vinti", "Tackle 1/3 campo", "Tackle meta campo", "Tackle Attacco",
                 "Tackle non Riusciti", "Pressing tentati", "Pressing succesfull",
                 "Percentuale successo", "Pressing 1/3", "Pressing meta campo", "Pressing attacco",
                 "Tiri Bloccati", "Passaggi Bloccati", "Intercettazioni", "Spazzate"
                 ]
            for tag in tags:
                a = tag.text.split()
                data.append(a)
                i=i+1
                if i>500:
                    data.pop(500)
            for tag1 in tags1:
                a = tag1.text.split()
                data1.append(a)
                ind = ind + 1
                if ((ind > 33) and (ind < 54)):
                    data.insert(num, str(a).replace("[","").replace("]"," ").replace("'",""))
                    num = num + 26
            i =519
            while (i > 0):
                data.pop(i)
                data.pop(i -2)
                data.pop(i - 5)
                data.pop(i - 7)
                data.pop(i - 15)
                data.pop(i-16)
                data.pop(i-17)
                data.pop(i-23)
                data.pop(i-24)
                i = i - 26
            i = 0
            ind = 0
            while ((i < 340)):
                data[i + 1] = p[ind] + " " + str(data[i + 1]).replace("[", "").replace("]", "").replace("'","")
                data[i + 2] = p[ind + 1] + " " + str(data[i + 2]).replace("[", "").replace("]", "").replace("'","")
                data[i + 3] = p[ind + 2] + " " + str(data[i + 3]).replace("[", "").replace("]", "").replace("'","")
                data[i + 4] = p[ind + 3] + " " + str(data[i + 4]).replace("[", "").replace("]", "").replace("'","")
                data[i + 5] = p[ind + 4] + " " + str(data[i + 5]).replace("[", "").replace("]", "").replace("'","")
                data[i + 6] = p[ind + 5] + " " + str(data[i + 6]).replace("[", "").replace("]", "").replace("'","")
                data[i + 7] = p[ind + 6] + " " + str(data[i + 7]).replace("[", "").replace("]", "").replace("'","")
                data[i + 8] = p[ind + 7] + " " + str(data[i + 8]).replace("[", "").replace("]", "").replace("'","")
                data[i + 9] = p[ind + 8] + " " + str(data[i + 9]).replace("[", "").replace("]", "").replace("'","")
                data[i + 10] = p[ind + 9] + " " + str(data[i + 10]).replace("[", "").replace("]", "").replace("'","")
                data[i + 11] = p[ind + 10] + " " + str(data[i + 11]).replace("[", "").replace("]", "").replace("'","")
                data[i + 12] = p[ind + 11] + " " + str(data[i + 12]).replace("[", "").replace("]", "").replace("'","")
                data[i + 13] = p[ind + 12] + " " + str(data[i + 13]).replace("[", "").replace("]", "").replace("'", "")
                data[i + 14] = p[ind + 13] + " " + str(data[i + 14]).replace("[", "").replace("]", "").replace("'", "")
                data[i + 15] = p[ind + 14] + " " + str(data[i + 15]).replace("[", "").replace("]", "").replace("'", "")
                data[i + 16] = p[ind + 15] + " " + str(data[i + 16]).replace("[", "").replace("]", "").replace("'", "") +"\n"
                i = i + 17
                ind = 0
            with open('DEFstats.json', 'w') as f:
                for prova in data:
                    f.write(str(prova))




    def estrpolaPossesso(self):
            html = requests.get('https://fbref.com/en/comps/11/possession/Serie-A-Stats').text
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.find_all('td')
            tags1 = soup.find_all('th')
            data=[]
            data1=[]
            ind=0
            num=0
            i=0
            p = ["Possesso%", "Tocchi", "Tocchi In area", "Tocchi 1/3 Campo", "Tocchi Metà",
                 "Tocchi attacco", "Tocchi area Avv: ", "Dribbling Riusciti ",
                 "Dribbling Tentati", "Percentuale", "Tunnel", "Minuti possesso",
                 "Distanza Possesso", "Distanza progressiva", "Ingressi 1/3 Avv: ", "Ingressi in area", "Anticipi", "Possessi persi"
                 ]
            for tag in tags:
                a = tag.text.split()
                data.append(a)
                i=i+1
                if i>540:
                    data.pop(540)
            for tag1 in tags1:
                a = tag1.text.split()
                data1.append(a)
                ind = ind + 1
                if ((ind > 34) and (ind < 55)):
                    data.insert(num, str(a).replace("[","").replace("]"," ").replace("'",""))
                    num = num + 26
            i =519
            while (i > 0):
                data.pop(i)
                data.pop(i -2)
                data.pop(i - 5)
                data.pop(i - 7)
                data.pop(i - 15)
                data.pop(i-16)
                data.pop(i-17)
                data.pop(i-23)
                data.pop(i-24)
                i = i - 26
            i = 0
            ind = 0
            while ((i <= 340)):
                data[i]=  str(data[i])
                data[i + 1] = p[ind] + " " + str(data[i + 1]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 2] = p[ind + 1] + " " + str(data[i + 2]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 3] = p[ind + 2] + " " + str(data[i + 3]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 4] = p[ind + 3] + " " + str(data[i + 4]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 5] = p[ind + 4] + " " + str(data[i + 5]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 6] = p[ind + 5] + " " + str(data[i + 6]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 7] = p[ind + 6] + " " + str(data[i + 7]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 8] = p[ind + 7] + " " + str(data[i + 8]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 9] = p[ind + 8] + " " + str(data[i + 9]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 10] = p[ind + 9] + " " + str(data[i + 10]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 11] = p[ind + 10] + " " + str(data[i + 11]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 12] = p[ind + 11] + " " + str(data[i + 12]).replace("[", "").replace("]", ",").replace("'","")
                data[i + 13] = p[ind + 12] + " " + str(data[i + 13]).replace("[", "").replace("]", ",").replace("'", "")
                data[i + 14] = p[ind + 13] + " " + str(data[i + 14]).replace("[", "").replace("]", ",").replace("'", "")
                data[i + 15] = p[ind + 14] + " " + str(data[i + 15]).replace("[", "").replace("]", ",").replace("'", "")
                data[i + 16] = p[ind + 15] + " " + str(data[i + 16]).replace("[", "").replace("]", ",").replace("'", "") + "\n"
                i = i + 17
                ind = 0
            i=34;
            with open('Squad.json', 'w') as f:
                while i<54:
                    f.write(str(data1[i]))
                    i=i+1
            with open('POSSstats.json', 'w') as f:
                while i<340:
                    f.write(str(data[i]))
                    i=i+1




    def estrpolaKeeper(self):
        html = requests.get('https://fbref.com/en/comps/11/keepersadv/Serie-A-Stats').text
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('td')
        tags1 = soup.find_all('th')
        data = []
        data1 = []
        ind = 0
        num = 0
        i = 0
        p = ["Goal Subiti", "GoalRigore", "GoalPunizioni", "Goalcorner", "Lanci completati oltre 35M",
             "Lanci tentati oltre 35m", "Percentuale", "Passaggi (escluso rinvio)",
             "Rilanci con mani", "Pressing 1/3", "Pressing meta campo", "Pressing attacco",
             "Tiri Bloccati", "Passaggi Bloccati", "Intercettazioni", "Spazzate"
             ]
        for tag in tags:
            a = tag.text.split()
            data.append(a)
            i = i + 1
            if i > 540:
                data.pop(540)
        for tag1 in tags1:
            a = tag1.text.split()
            data1.append(a)
            ind = ind + 1
            if ((ind > 37) and (ind < 58)):

                data.insert(num, str(a).replace("[","").replace("]"," ").replace("'",""))
                num = num + 26


        i = 519
        while (i > 0):
            data.pop(i)
            data.pop(i - 2)
            data.pop(i - 5)
            data.pop(i - 7)
            data.pop(i - 15)
            data.pop(i - 16)
            data.pop(i - 17)
            data.pop(i - 23)
            data.pop(i - 24)
            i = i - 26
        i = 0
        ind = 0
        while ((i < 340)):
            data[i + 1] = p[ind] + " " + str(data[i + 1]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 2] = p[ind + 1] + " " + str(data[i + 2]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 3] = p[ind + 2] + " " + str(data[i + 3]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 4] = p[ind + 3] + " " + str(data[i + 4]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 5] = p[ind + 4] + " " + str(data[i + 5]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 6] = p[ind + 5] + " " + str(data[i + 6]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 7] = p[ind + 6] + " " + str(data[i + 7]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 8] = p[ind + 7] + " " + str(data[i + 8]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 9] = p[ind + 8] + " " + str(data[i + 9]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 10] = p[ind + 9] + " " + str(data[i + 10]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 11] = p[ind + 10] + " " + str(data[i + 11]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 12] = p[ind + 11] + " " + str(data[i + 12]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 13] = p[ind + 12] + " " + str(data[i + 13]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 14] = p[ind + 13] + " " + str(data[i + 14]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 15] = p[ind + 14] + " " + str(data[i + 15]).replace("[", "").replace("]", "").replace("'", "")
            data[i + 16] = p[ind + 15] + " " + str(data[i + 16]).replace("[", "").replace("]", "").replace("'", "")+"\n"
            i = i + 17
            ind = 0


        i=0
        with open('Keeper.json', 'w') as f:
            while i < 340:
                f.write(str(data[i]))
                i = i + 1
