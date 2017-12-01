import telepot
import time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import numpy as np
import time
from PIL import Image
import string
import random

t = int(time.time()*1000.0)
random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
idlist=[]
namelist=[]
order=[]
territori=[[0,1,2,3,4,5,6,7,8],[9,10,11,12],[13,14,15,16,17,18,19],[20,21,22,23,24,25],[26,27,28,29,30,31,32,33,34,35,36,37],[38,39,40,41]]
#North America, South America, Europe, Africa, Asia, Oceania
confini=[[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], #Alaska
         [1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Northwest_Territory
         [0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Greenland
         [1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Alberta
         [0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Ontario
         [0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Quebec
         [0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Western_United_States
         [0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Eastern_United_States
         [0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Central_America
         [0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Venezuela
         [0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Peru
         [0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Brasil
         [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Argentina
         [0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Iceland
         [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Scandinavia
         [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Great_Britain
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Northern_Europe
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Western_Europe
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], #Southern_Europe
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0], #Ukraine
         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #North_Africa
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], #Egypt
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Congo
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #East_Africa
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #South_Africa
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Madagascar
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0], #Ural
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0], #Siberia
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0], #Yakutsk
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0], #Irkutsk
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0], #Kamchatka
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0], #Japan
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,0,0], #Mongolia
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0], #Afghanistan
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0], #Middle_East
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0], #India
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0], #China
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0], #Siam
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1], #Indonesia
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1], #New_Guinea
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], #Eastern_Australia
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]] #Western_Australia
territori_nomi=['Alaska','Northwest_Territory','Greenland','Alberta','Ontario','Quebec','Western_United_States','Eastern_United_States',
    'Central_America','Venezuela','Peru','Brasil','Argentina','Iceland','Scandinavia','Great_Britain','Northern_Europe','Western_Europe',
    'Southern_Europe','Ukraine','North_Africa','Egypt','Congo','East_Africa','South_Africa','Madagascar','Ural','Siberia','Yakutsk',
    'Irkutsk','Kamchatka','Japan','Mongolia','Afghanistan','Middle_East','India','China','Siam','Indonesia','Nuova_Guinea',
    'Eastern_Australia','Western_Australia']
terr=[]
lista_terr=''
aspetta=True
truppe_terr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
truppe_disponibili=0
obiettivi_testo=['Presidia 18 territori con almeno due truppe ciascuno','Conquista 24 territori','Conquista Nord America e Africa',
    'Conquista Nord America e Oceania','Conquista Asia e Sud America','Conquista Asia e Arfica',
    'Conquista Europa, Sud America e un terzo continente a scelta','Conquista Europa, Oceania e un terzo continente a scelta']
obiettivi_posseduti=range(len(obiettivi_testo))
preparativi=True
prossimo_giocatore=0
mask=[]
colori_terr=[]
for i in range(len(territori_nomi)):
    colori_terr.append([i,255,255])
colori_players=[[0,255,0,255],[255,0,0,255],[0,0,255,255],[255,0,255,255],[255,255,0,255],[255,128,0,255]]

def ordine_turni(): #crea casualmente un ordine tra i giocatori
    print('ordine_turni')
    global order
    random.shuffle(order)

def dividi_territori(): #divide casualmente i vari territori tra i giocatori
    print('dividi_territori')
    global terr
    terr=((len(territori_nomi)-1)//len(idlist)+1)*order
    random.shuffle(terr)
    terr.reverse()
    for i in range(len(terr)-len(territori_nomi)):
        terr.remove(len(idlist)-i-1)
    terr.reverse
    for i in range(len(territori)):
        for j in range(len(territori[i])):
            territori[i][j]=terr[territori[i][j]]

def territori_posseduti(n):   #crea una lista per mandare un messaggio ad ogni giocatore con i propri territori
    global territori
    print(territori)
    global lista_terr
    lista_terr=''
    contatore=-1
    for i in range(len(territori)):
        for j in range(len(territori[i])):
            contatore+=1
            if territori[i][j]==n:
                lista_terr+=('\n '+territori_nomi[contatore]+'\t'+str(truppe_terr[contatore]))
    return lista_terr

def num_terr_poss(n):   #determina il numero dei territori del giocatore n
    print('num_terr_poss')
    cont=0
    for i in range(len(territori)):
        for j in range(len(territori[i])):
            if territori[i][j]==n:
                cont+=1
    return cont

def colora():   #colora e invia la mappa
    print('colora')
    global mask
    global idlist
    im=Image.open('plancia.tif')
    im=im.convert('RGBA')
    data=np.array(im)
    rgb=data[:,:,:3]
    for i in range(len(territori_nomi)):
        mask.append(np.all(rgb==colori_terr[i],axis=-1))
    contatore=0
    for i in range(len(territori)):
        for j in range(len(territori[i])):
            data[mask[contatore]]=colori_players[territori[i][j]]
            contatore+=1
    im=Image.fromarray(data)
    im=im.convert('RGB')
    im.save('im.jpg')
    f=open('im.jpg', 'rb')
    for i in range(len(idlist)):
        f.seek(0)
        bot.sendPhoto(idlist[i],f)

def nuove_truppe(n):    #nuove truppe esclusi eventuali tris
    print('nuove_truppe')
    truppe=0
    for i in range(len(territori)):
        for j in range(len(territori[i])):
            if territori[i][j]==n:
                truppe+=1
    truppe=truppe//3
    if territori[0]==[n,n,n,n,n,n,n,n,n]:
        truppe+=5
    if territori[1]==[n,n,n,n]:
        truppe+=2
    if territori[2]==[n,n,n,n,n,n,n]:
        truppe+=5
    if territori[3]==[n,n,n,n,n,n]:
        truppe+=5
    if territori[4]==[n,n,n,n,n,n,n,n,n,n,n,n]:
        truppe+=7
    if territori[5]==[n,n,n,n]:
        truppe+=2
    return truppe

def dividi_obiettivi(): #permuta gli obiettivi
    print('dividi_obiettivi')
    global obiettivi_posseduti
    random.shuffle(obiettivi_posseduti)

def obiettivi(n):   #ritorna l'obiettivo del giocatore n
    print('obiettivi')
    return obiettivi_testo[obiettivi_posseduti[idlist.index(n)]]

def vivo(n):    #controlla se il giocatore è ancora vivo
    print('vivo')
    vivo_temp=False
    for i in range(len(territori)):
        if territori[i].count!=0:
            vivo_temp=True
    return vivo_temp

def rinforzo():    #funzione che gestisce il rinforzo
    print('rinforzo')
    if vivo(order.index(prossimo_giocatore)):
        bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai {} nuove truppe da disporre nei seguenti territori:'.format(nuove_truppe(order.index(prossimo_giocatore)))+territori_posseduti(order.index(prossimo_giocatore)))
        bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Disponile scrivendo "Rinforzo x1, x2, x3, ..."')

def attacchi_possibili(n):  #funzione che controlla gli stati nemici confinanti che si possono attaccare
    print('attacchi_possibili')
    global lista_terr
    lista_terr=''
    check=True
    contatore=-1
    for i in range(len(territori)):
        for j in range(len(territori[i])):
            contatore+=1
            if territori[i][j]==n:
                for h in range(len(territori_nomi)):
                    indice=h
                    continente=0
                    for l in range(len(territori)):
                        if indice>=len(territori[l]) and check:
                            indice-=len(territori[l])
                            continente+=1
                        else:
                            check=False
                        print("contatore\th\tcontinente\tindice\tl\tlen(territori[l])")
                        print(contatore,"\t\t",h,"\t",continente,"\t\t",indice,"\t",l,"\t",len(territori[l]))
                    if confini[contatore][h]==1 and territori[continente][indice]!=n and truppe_terr[contatore]>1 and (territori_nomi[h] not in lista_terr):
                        lista_terr+=('\n'+territori_nomi[h]+'\t'+str(truppe_terr[h]))
    return lista_terr

def  obiettivo_raggiunto(n):    #controlla se il giocatore n ha raggiunto il suo obiettivo
    print('obiettivo_raggiunto')
    if obiettivi_posseduti[n]==0:
        for i in range(len(territori_nomi)):
            contatore=0
            if terr[i]==n and truppe_terr[i]>=2:
                contatore+=1
        return contatore>=18
    elif obiettivi_posseduti[n]==1:
        return terr.count(n)>=24
    elif obiettivi_posseduti[n]==2:
        return (territori[0]==[n,n,n,n,n,n,n,n,n] and territori[3]==[n,n,n,n,n,n])
    elif obiettivi_posseduti[n]==3:
        return (territori[0]==[n,n,n,n,n,n,n,n,n] and territori[5]==[n,n,n,n])
    elif obiettivi_posseduti[n]==4:
        return (territori[1]==[n,n,n,n] and territori[4]==[n,n,n,n,n,n,n,n,n,n,n,n])
    elif obiettivi_posseduti[n]==5:
        return (territori[3]==[n,n,n,n,n,n] and territori[4]==[n,n,n,n,n,n,n,n,n,n,n,n])
    elif obiettivi_posseduti[n]==6:
        parziale=territori[0]==[n,n,n,n,n,n,n,n,n] or territori[3]==[n,n,n,n,n,n] or territori[4]==[n,n,n,n,n,n,n,n,n,n,n,n] or territori[5]==[n,n,n,n]
        return (territori[1]==[n,n,n,n] and territori[2]==[n,n,n,n,n,n,n] and parziale)
    elif obiettivi_posseduti[n]==7:
        parziale=territori[0]==[n,n,n,n,n,n,n,n,n] or territori[1]==[n,n,n,n] or territori[3]==[n,n,n,n,n,n] or territori[4]==[n,n,n,n,n,n,n,n,n,n,n,n]
        return (territori[2]==[n,n,n,n,n,n,n] and territori[5]==[n,n,n,n] and parziale)

def attacco():  #funzione che gestisce l'attacco
    print('attacco')
    if vivo(order.index(prossimo_giocatore)):
        bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai la seguente situazione:'+territori_posseduti(order.index(prossimo_giocatore))+'\n e puoi attaccare i seguenti stati:'+attacchi_possibili(order.index(prossimo_giocatore)))
        bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Attacca scrivendo "Attacca" e il nome dello stato da cui attaccare, il nome dello stato da attaccare e il numero di truppe che vuoi utilizzare, oppure "Spostamento" per terminare la fase di attacco')

def spostamento():  #funzione che gestisce lo spostamento
    print('spostamento')
    if vivo(order.index(prossimo_giocatore)):
        bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai la seguente situazione:'+territori_posseduti(order.index(prossimo_giocatore)))
        bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Sposta scrivendo "Sposta" e il nome dello stato di partenza, il nome dello stato di arrivo e il numero di truppe che vuoi spostare, oppure "Fine" per terminare il turno')

def lancio_dadi(n,m):   #funzione che determina l'esito di un attacco
    print('lancio_dadi')
    d1=np.random.random_integers(1,6,n)
    d2=np.random.random_integers(1,6,m)
    d1=np.sort(d1)
    d2=np.sort(d2)
    res=[0,0]
    print("d1")
    for i in range(len(d1)):
        print(d1[i])
    print("d2")
    for i in range(len(d2)):
        print(d2[i])
    for i in range(min(len(d1),len(d2))):
        if d1[len(d1)-i-1]>d2[len(d2)-i-1]:
            res[1]+=1
        else:
            res[0]+=1
    return res

def on_chat_message(msg):
    global preparativi
    global prossimo_giocatore
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Contact from ', chat_id)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        global idlist
        global truppe_terr
        if txt.startswith('/start') and aspetta:
            nuovo=True
            for i in range(len(idlist)):
                if chat_id == idlist[i]:
                    nuovo=False
            if len(idlist)<6 and nuovo:
                global namelist
                global order
                idlist.append(chat_id)
                namelist.append(name)
                order.append(len(idlist)-1)
                for i in range(len(idlist)):
                    bot.sendMessage(idlist[i], 'Ciao {}, siamo a {} giocatori'.format(namelist[i],len(idlist)))
                if len(idlist)>2:
                    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Sì', callback_data='/inizio'),InlineKeyboardButton(text='No', callback_data='void')]])
                    bot.sendMessage(idlist[0], 'Iniziamo?', reply_markup=keyboard)
        elif txt.startswith('Posiziona') and preparativi:
            params=txt.split()[1:]
            check=True
            try:
                params=[int(param) for param in params]
            except:
                bot.sendMessage(chat_id,'Errore nei parametri, non hai inserito numeri!')
            if len(params)<num_terr_poss(idlist.index(chat_id)):
                check=False
                bot.sendMessage(chat_id, 'Ogni territorio deve avere almeno una truppa')
            if sum(params)!=50-5*len(idlist):
                check=False
                bot.sendMessage(chat_id, 'Il numero totale di truppe è errato')
            if check:
                print('truppe prese')
                k=-1
                l=-1
                for i in range(len(territori)):
                    for j in range(len(territori[i])):
                        k+=1
                        if territori[i][j]==idlist.index(chat_id):
                            l+=1
                            truppe_terr[k]=params[l]
                            if truppe_terr.count(0)==0:
                                preparativi=False
                                rinforzo()
        elif txt.startswith('Rinforzo') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params = txt.split()[1:]
            check=True
            try:
                params=[int(param) for param in params]
            except:
                check=False
                bot.sendMessage(chat_id,'Errore nei parametri, non hai inserito numeri!')
            if sum(params)!=nuove_truppe(idlist.index(chat_id)):
                check=False
                bot.sendMessage(chat_id, 'La somma delle truppe è errata')
            if len(params)!=num_terr_poss(idlist.index(chat_id)):
                check=False
                bot.sendMessage(chat_id, 'Il numero di truppe è errato')
            if check:
                k=-1
                l=-1
                for i in range(len(territori)):
                    for j in range(len(territori[i])):
                        k+=1
                        if territori[i][j]==idlist.index(chat_id):
                            l+=1
                            truppe_terr[k]+=params[l]
                colora()
                attacco()
        elif txt.startswith('Attacca') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params=txt.split()[1:]
            if len(params)==3:
                if params[0] in territori_posseduti(order.index(prossimo_giocatore)):
                    if confini[territori_nomi.index(params[0])][territori_nomi.index(params[1])]==1:
                        if int(params[2])<truppe_terr[territori_nomi.index(params[0])]:
                            truppe_attacco=int(params[2])
                            truppe_terr[territori_nomi.index(params[0])]-=truppe_attacco
                            while truppe_attacco>0 and truppe_terr[territori_nomi.index(params[1])]>0:
                                if truppe_attacco>3:
                                    if truppe_terr[territori_nomi.index(params[1])]>3:
                                        res=lancio_dadi(3,3)
                                    else:
                                        res=lancio_dadi(3,truppe_terr[territori_nomi.index(params[1])])
                                else:
                                    if truppe_terr[territori_nomi.index(params[1])]>3:
                                        res=lancio_dadi(truppe_attacco,3)
                                    else:
                                        res=lancio_dadi(truppe_attacco,truppe_terr[territori_nomi.index(params[1])])
                                truppe_attacco-=res[0]
                                truppe_terr[territori_nomi.index(params[1])]-=res[1]
                            if truppe_terr[territori_nomi.index(params[1])]<1:
                                truppe_terr[territori_nomi.index(params[1])]=truppe_attacco
                                indice=territori_nomi.index(params[1])
                                continente=0
                                for i in range(len(territori)):
                                    if indice>=len(territori[i]):
                                        indice-=len(territori[i])
                                        continente+=1
                                territori[continente][indice]=order.index(prossimo_giocatore)
                                colora()
                                if obiettivo_raggiunto(order.index(prossimo_giocatore)):
                                    for i in range(idlist):
                                        bot.sendMessage(idlist[i], 'Il giocatore {}, '.format(prossimo_giocatore+1)+'cioè {}, ha vinto la partita'.format(namelist[order.index(prossimo_giocatore)]))
                                    bot.sendMessage(idlist[order.index(prossimo_giocatore)], 'Hai vinto la partita!')
                                else:
                                    attacco()
                            else:
                                attacco()
                        else:
                            bot.sendMessage(idlist[order.index(prossimo_giocatore)], 'Devi lasciare nello stato almeno 1 truppa!')
                            attacco()
                    else:
                        bot.sendMessage(idlist[order.index(prossimo_giocatore)], '{} non confina con lo stato da te scelto!'.format(params[1]))
                        attacco()
                else:
                    bot.sendMessage(idlist[order.index(prossimo_giocatore)], '{} non ti appartiene!'.format(params[0]))
                    attacco()
        elif txt.startswith('Spostamento') and idlist[order.index(prossimo_giocatore)]==chat_id:
            spostamento()
        elif txt.startswith('Sposta') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params=txt.split()[1:]
            if len(params)==3:
                if params[0] in territori_posseduti(order.index(prossimo_giocatore)):
                    if params[1] in territori_posseduti(order.index(prossimo_giocatore)):
                        if int(params[2])<truppe_terr[territori_nomi.index(params[1])]:
                            if confini[territori_nomi.index(params[0])][territori_nomi.index(params[1])]==1:
                                truppe_terr[territori_nomi.index(params[0])]-=params[2]
                                truppe_terr[territori_nomi.index(params[1])]+=params[2]
                                colora()
                                prossimo_giocatore=(prossimo_giocatore+1)%len(idlist)
                                rinforzo()
        elif txt.startswith('Fine') and idlist[order.index(prossimo_giocatore)]==chat_id:
            prossimo_giocatore=(prossimo_giocatore+1)%len(idlist)
            rinforzo()

def on_callback_query(msg): #aziona i vari LED in base al pulsante toccato
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    if query_data == '/inizio':
        aspetta = False

        global idlist
        global order
        ordine_turni()
        dividi_territori()
        global truppe_disponibili
        for i in range(len(idlist)):
            bot.sendMessage(idlist[i], 'Lancio dei dadi per decidere chi inizia...\nSei il giocatore n.{}'.format(order[i]+1))
            bot.sendMessage(idlist[i], 'Hai i seguenti territori:'+territori_posseduti(i)+'\nE questo obiettivo: '+obiettivi(idlist[i]))
            bot.sendMessage(idlist[i], 'Hai a disposizione {} truppe, disponile nei tuoi territori scrivendo "Posiziona x1 x2 x3 ..." con x1, x2, x3, ... il numero di truppe da mettere in ogni territorio'.format(50-5*len(idlist)))
        colora()

bot=telepot.Bot('*INSERT YOUR TOKEN HERE*')
bot.message_loop({'chat': on_chat_message,'callback_query': on_callback_query})
print ('Listening ...')

while 1:
    time.sleep(10)
