import telepot
import time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import numpy as np
import time
from PIL import Image
import string
import random

idlist=[]
namelist=[]
order=[]
territories=[[0,1,2,3,4,5,6,7,8],[9,10,11,12],[13,14,15,16,17,18,19],[20,21,22,23,24,25],[26,27,28,29,30,31,32,33,34,35,36,37],[38,39,40,41]]
#North America, South America, Europe, Africa, Asia, Oceania
borders=[[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], #Alaska
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
territories_names=['Alaska','Northwest_Territory','Greenland','Alberta','Ontario','Quebec','Western_United_States','Eastern_United_States',
    'Central_America','Venezuela','Peru','Brasil','Argentina','Iceland','Scandinavia','Great_Britain','Northern_Europe','Western_Europe',
    'Southern_Europe','Ukraine','North_Africa','Egypt','Congo','East_Africa','South_Africa','Madagascar','Ural','Siberia','Yakutsk',
    'Irkutsk','Kamchatka','Japan','Mongolia','Afghanistan','Middle_East','India','China','Siam','Indonesia','Nuova_Guinea',
    'Eastern_Australia','Western_Australia']
terr=[]
terr_list=''
wait=True
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
for i in range(len(territories_names)):
    colori_terr.append([i,255,255])
colori_players=[[0,255,0,255],[255,0,0,255],[0,0,255,255],[255,0,255,255],[255,255,0,255],[255,128,0,255]]
cifra0=Image.open('0.tif')
cifra1=Image.open('1.tif')
cifra2=Image.open('2.tif')
cifra3=Image.open('3.tif')
cifra4=Image.open('4.tif')
cifra5=Image.open('5.tif')
cifra6=Image.open('6.tif')
cifra7=Image.open('7.tif')
cifra8=Image.open('8.tif')
cifra9=Image.open('9.tif')
cifre=[cifra0,cifra1,cifra2,cifra3,cifra4,cifra5,cifra6,cifra7,cifra8,cifra9]
posizione=[[120,120],[210,160],[470,85],[160,230],[260,280],[355,300],[120,310],[200,365],[100,410],[180,500],[160,635],[250,580],[170,700],[540,165],[610,220],[520,280],
            [600,320],[490,390],[610,390],[710,320],[520,560],[640,540],[610,650],[700,630],[640,750],[750,750],[800,260],[850,210],[930,120],[940,220],[1010,110],[1140,220],  #Giappone
            [990,270],[820,350],[800,490],[940,490],[1020,360],[1040,470],[1120,570],[1200,630],[1170,780],[1080,760]]
tris=['fante','cannone','cavallo','fante','cavallo','cannone','fante','canone','cavallo','cannone','cavallo','cannone','fante','fante','cannone','cavallo','cavallo','fante','cavallo','cannone','fante','fante','cavallo','cannone',
        'cannone','fante','cavallo','cannone','cavallo','fante','cavallo','fante','cannone','fante','cannone','fante','cavallo','cannone','cavallo','cavallo','fante','cannone','jolly','jolly']
tris_num=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
tris_usati=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,]
carta_territorio=False
tris_cont=0
truppe_tris=0

def ordine_turni(): #creates a random order among the players
    print('ordine_turni')
    global order
    t = int(time.time()*1000.0)
    random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
    random.shuffle(order)

def dividi_territori(): #divides randomly the territories among the players
    print('dividi_territori')
    global terr
    terr=((len(territories_names)-1)//len(idlist)+1)*order
    t = int(time.time()*1000.0)
    random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
    random.shuffle(terr)
    terr.reverse()
    for i in range(len(terr)-len(territories_names)):
        terr.remove(len(idlist)-i-1)
    terr.reverse
    for i in range(len(territories)):
        for j in range(len(territories[i])):
            territories[i][j]=terr[territories[i][j]]

def territori_posseduti(n):   #creates a list with all the territories owned by player n
    global territories
    print('territori_posseduti')
    global terr_list
    terr_list=''
    counter=-1
    for i in range(len(territories)):
        for j in range(len(territories[i])):
            counter+=1
            if territories[i][j]==n:
                terr_list+=('\n '+territories_names[counter]+'\t'+str(truppe_terr[counter]))
    return terr_list

def num_terr_poss(n):   #returns the number of territories ownes by player n
    print('num_terr_poss')
    cont=0
    for i in range(len(territories)):
        for j in range(len(territories[i])):
            if territories[i][j]==n:
                cont+=1
    return cont

def colora():   #colours and sends the map
    print('colora')
    global mask
    global idlist
    im=Image.open('world.tif')
    im=im.convert('RGBA')
    data=np.array(im)
    rgb=data[:,:,:3]
    for i in range(len(territories_names)):
        mask.append(np.all(rgb==colori_terr[i],axis=-1))
    counter=0
    for i in range(len(territories)):
        for j in range(len(territories[i])):
            data[mask[counter]]=colori_players[territories[i][j]]
            counter+=1
    im=Image.fromarray(data)
    im=im.convert('RGB')
    for i in range(len(truppe_terr)):   #writes the number of troops of each territory
        j=0
        while 10**j<=truppe_terr[i]:
            cifra=(truppe_terr[i]//(10**j))%10
            im.paste(cifre[cifra],(posizione[i][0]-12*j,posizione[i][1],posizione[i][0]-12*(j-1),posizione[i][1]+19))
            j+=1
    im.save('im.jpg')
    f=open('im.jpg', 'rb')
    for i in range(len(idlist)):
        f.seek(0)
        bot.sendPhoto(idlist[i],f)

def nuove_truppe(n):    #calculates the number of new troops of player n
    print('nuove_truppe')
    global truppe_tris
    truppe=truppe_tris
    truppe_tris=0
    for i in range(len(territories)):
        for j in range(len(territories[i])):
            if territories[i][j]==n:
                truppe+=1
    truppe=truppe//3
    if territories[0]==[n,n,n,n,n,n,n,n,n]:
        truppe+=5
    if territories[1]==[n,n,n,n]:
        truppe+=2
    if territories[2]==[n,n,n,n,n,n,n]:
        truppe+=5
    if territories[3]==[n,n,n,n,n,n]:
        truppe+=5
    if territories[4]==[n,n,n,n,n,n,n,n,n,n,n,n]:
        truppe+=7
    if territories[5]==[n,n,n,n]:
        truppe+=2
    return truppe

def dividi_obiettivi(): #permuta gli obiettivi
    print('dividi_obiettivi')
    global obiettivi_posseduti
    t = int(time.time()*1000.0)
    random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
    random.shuffle(obiettivi_posseduti)

def obiettivi(n):   #ritorna l'obiettivo del giocatore n
    print('obiettivi')
    return obiettivi_testo[obiettivi_posseduti[idlist.index(n)]]

def vivo(n):    #controlla se il giocatore è ancora vivo
    print('vivo')
    vivo_temp=False
    for i in range(len(territories)):
        if territories[i].count!=0:
            vivo_temp=True
    return vivo_temp

def mischia_tris(): #mischia il mazzo delle carte teriitorio
    print('mischia_tris')
    global tris_num
    tris_scambio=[]
    tris_provvisorio=[]
    for i in range(len(tris_num)):
        if tris_usati[i]==-1:
            tris_scambio.append(tris_num[i])
            tris_provvisorio.append(0)
    t = int(time.time()*1000.0)
    random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
    random.shuffle(tris_scambio)
    for i in range(len(tris_scambio)):
        tris_provvisorio[i]=tris_num[tris_scambio[i]]
    indice=0
    for i in range(len(tris_num)):
        if tris_usati[i]==-1:
            tris_num[i]=tris_provvisorio[indice]
            indice+=1

def tris_posseduti(n):
    print('tris_posseduti')
    global tris_num
    global tris_usati
    lista_tris=''
    for i in range(len(tris_usati)):
        if tris_usati[i]==n:
            lista_string+=('\n'+territori_names[tris_num[i]+' '+tris[tris_num[i]]])
    return lista_tris

def tris():
    print('tris')
    if(tris_usati.count(i)>0):
        if vivo(order.index(prossimo_giocatore)):
            bot.sendMessage(idlist[order.index(prossimo_giocatore)], 'Hai le seguenti carte territorio: {}'.format(tris_posseduti(order.index(prossimo_giocatore))))
            bot.sendMessage(idlist[order.index(prossimo_giocatore)], 'Gioca un tris scrivendo "Tris territorio1 territorio2 territorio3", oppure "Salta" per passare alla fase di rinforzo')
        else:
            prossimo_giocatore+=1
            tris()
    else:
        rinforzo()

def rinforzo():    #funzione che gestisce il rinforzo
    print('rinforzo')
    mischia_tris()
    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai {} nuove truppe da disporre nei seguenti territori:'.format(nuove_truppe(order.index(prossimo_giocatore)))+territori_posseduti(order.index(prossimo_giocatore)))
    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Disponile scrivendo "Rinforzo x1 x2 x3 ..."')

def attacchi_possibili(n):  #funzione che controlla gli stati nemici confinanti che si possono attaccare
    print('attacchi_possibili')
    global terr_list
    terr_list=''
    counter=-1
    for i in range(len(territories)):
        for j in range(len(territories[i])):
            counter+=1
            if territories[i][j]==n:
                for h in range(len(territories_names)):
                    indice=h
                    continente=0
                    check=True
                    for l in range(len(territories)):
                        if indice>=len(territories[l]) and check:
                            indice-=len(territories[l])
                            continente+=1
                        else:
                            check=False
                    if borders[counter][h]==1 and territories[continente][indice]!=n and truppe_terr[counter]>1 and (territori_nameses[h] not in terr_list):
                        terr_list+=('\n'+territories_names[h]+'\t'+str(truppe_terr[h]))
    return terr_list

def  obiettivo_raggiunto(n):    #controlla se il giocatore n ha raggiunto il suo obiettivo
    print('obiettivo_raggiunto')
    if obiettivi_posseduti[n]==0:
        for i in range(len(territories_names)):
            counter=0
            if terr[i]==n and truppe_terr[i]>=2:
                counter+=1
        return counter>=18
    elif obiettivi_posseduti[n]==1:
        return terr.count(n)>=24
    elif obiettivi_posseduti[n]==2:
        return (territories[0]==[n,n,n,n,n,n,n,n,n] and territories[3]==[n,n,n,n,n,n])
    elif obiettivi_posseduti[n]==3:
        return (territories[0]==[n,n,n,n,n,n,n,n,n] and territories[5]==[n,n,n,n])
    elif obiettivi_posseduti[n]==4:
        return (territories[1]==[n,n,n,n] and territories[4]==[n,n,n,n,n,n,n,n,n,n,n,n])
    elif obiettivi_posseduti[n]==5:
        return (territories[3]==[n,n,n,n,n,n] and territories[4]==[n,n,n,n,n,n,n,n,n,n,n,n])
    elif obiettivi_posseduti[n]==6:
        parziale=territories[0]==[n,n,n,n,n,n,n,n,n] or territories[3]==[n,n,n,n,n,n] or territories[4]==[n,n,n,n,n,n,n,n,n,n,n,n] or territories[5]==[n,n,n,n]
        return (territories[1]==[n,n,n,n] and territories[2]==[n,n,n,n,n,n,n] and parziale)
    elif obiettivi_posseduti[n]==7:
        parziale=territories[0]==[n,n,n,n,n,n,n,n,n] or territories[1]==[n,n,n,n] or territories[3]==[n,n,n,n,n,n] or territories[4]==[n,n,n,n,n,n,n,n,n,n,n,n]
        return (territories[2]==[n,n,n,n,n,n,n] and territories[5]==[n,n,n,n] and parziale)

def attacco():  #funzione che gestisce l'attacco
    print('attacco')
    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai la seguente situazione:'+territori_posseduti(order.index(prossimo_giocatore))+'\n e puoi attaccare i seguenti stati:'+attacchi_possibili(order.index(prossimo_giocatore)))
    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Attacca scrivendo "Attacca" e il nome dello stato da cui attaccare, il nome dello stato da attaccare e il numero di truppe che vuoi utilizzare, oppure "Spostamento" per terminare la fase di attacco')

def spostamento():  #funzione che gestisce lo spostamento
    print('spostamento')
    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai la seguente situazione:'+territori_posseduti(order.index(prossimo_giocatore)))
    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Sposta scrivendo "Move" e il nome dello stato di partenza, il nome dello stato di arrivo e il numero di truppe che vuoi spostare, oppure "Fine" per terminare il turno')

def lancio_dadi(n,m):   #funzione che determina l'esito di un attacco
    print('lancio_dadi')
    t = int(time.time()*1000.0)
    random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
    d1=np.random.random_integers(1,6,n)
    t = int(time.time()*1000.0)
    random.seed(((t & 0xff000000)>>24)+((t & 0x00ff0000)>>8)+((t & 0x0000ff00)<<8)+((t & 0x000000ff)<<24))
    d2=np.random.random_integers(1,6,m)
    d1=np.sort(d1)
    d2=np.sort(d2)
    res=[0,0]
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
        global carta_territorio
        if txt.startswith('/start') and wait:
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
                for i in range(len(territories)):
                    for j in range(len(territories[i])):
                        k+=1
                        if territories[i][j]==idlist.index(chat_id):
                            l+=1
                            truppe_terr[k]=params[l]
                            if truppe_terr.count(0)==0:
                                preparativi=False
                                tris()
        elif txt.startswith('Tris') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params=txt.split()[1:]
            check=True
            if len(params)!=3:
                check=False
                bot.sendMessage(chat_id,'Non hai inserito tre carte')
            else:
                for i in range(3):
                    if params[i] not in territories_names:
                        check=False
                if not check:
                    bot.sendMessage(chat_id,'I names delle carte sono errati')
                else:
                    for i in range(3):
                        if tris_usati[territories_names.index(params[i])]!=prossimo_giocatore:
                            check=False
                    if not check:
                        bot.sendMessage(chat_id,'Hai inserito carte che non ti appartengono')
                    else:
                        if tris[territories_names.index(params[0])]==tris[territories_names.index(params[1])]==tris[territories_names.index(params[2])]=='cannone' or (tris[territories_names.index(params[1])]==tris[territories_names.index(params[2])]=='cannone' and tris[territories_names.index(params[0])]=='jolly') or (tris[territories_names.index(params[0])]==tris[territories_names.index(params[2])]=='canone' and tris[territories_names.index(params[1])]=='jolly') or (tris[territories_names.index(params[0])]==tris[territories_names.index(params[1])]=='cannone' and tris[territories_names.index(params[2])]=='jolly'):
                            truppe_tris=4
                        elif tris[territories_names.index(params[0])]==tris[territories_names.index(params[1])]==tris[territories_names.index(params[2])]=='fante' or (tris[territories_names.index(params[1])]==tris[territories_names.index(params[2])]=='fante' and tris[territories_names.index(params[0])]=='jolly') or (tris[territories_names.index(params[0])]==tris[territories_names.index(params[2])]=='fante' and tris[territories_names.index(params[1])]=='jolly') or (tris[territories_names.index(params[0])]==tris[territories_names.index(params[1])]=='fante' and tris[territories_names.index(params[2])]=='jolly'):
                            truppe_tris=6
                        elif tris[territories_names.index(params[0])]==tris[territories_names.index(params[1])]==tris[territories_names.index(params[2])]=='cavallo' or (tris[territories_names.index(params[1])]==tris[territories_names.index(params[2])]=='cavallo' and tris[territories_names.index(params[0])]=='jolly') or (tris[territories_names.index(params[0])]==tris[territories_names.index(params[2])]=='cavallo' and tris[territories_names.index(params[1])]=='jolly') or (tris[territories_names.index(params[0])]==tris[territories_names.index(params[1])]=='cavallo' and tris[territories_names.index(params[2])]=='jolly'):
                            truppe_tris=8
                        for i in range(3):
                            indice=territories_names.index(params[i])
                            check=True
                            for l in range(len(territories)):
                                if indice>=len(territories[l]) and check:
                                    indice-=len(territories[l])
                                    continente+=1
                                else:
                                    check=False
                            if territories[continente][indice]==prossimo_giocatore:
                                truppe_terr[territori_names.index(params[i])]+=2
                    rinforzo()
        elif txt.startswith('Rinforzo') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params=txt.split()[1:]
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
                for i in range(len(territories)):
                    for j in range(len(territories[i])):
                        k+=1
                        if territories[i][j]==idlist.index(chat_id):
                            l+=1
                            truppe_terr[k]+=params[l]
                colora()
                carta_territorio=False
                attacco()
        elif txt.startswith('Attacca') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params=txt.split()[1:]
            if len(params)==3:
                if params[0] in territori_posseduti(order.index(prossimo_giocatore)):
                    if borders[territori_names.index(params[0])][territori_names.index(params[1])]==1:
                        if int(params[2])<truppe_terr[territori_names.index(params[0])]:
                            truppe_attacco=int(params[2])
                            truppe_terr[territories_names.index(params[0])]-=truppe_attacco
                            while truppe_attacco>0 and truppe_terr[territories_names.index(params[1])]>0:
                                if truppe_attacco>3:
                                    if truppe_terr[territories_names.index(params[1])]>3:
                                        res=lancio_dadi(3,3)
                                    else:
                                        res=lancio_dadi(3,truppe_terr[territories_names.index(params[1])])
                                else:
                                    if truppe_terr[territories_names.index(params[1])]>3:
                                        res=lancio_dadi(truppe_attacco,3)
                                    else:
                                        res=lancio_dadi(truppe_attacco,truppe_terr[territories_names.index(params[1])])
                                truppe_attacco-=res[0]
                                truppe_terr[territories_names.index(params[1])]-=res[1]
                            if truppe_terr[territories_names.index(params[1])]<1:
                                truppe_terr[territories_names.index(params[1])]=truppe_attacco
                                indice=territories_names.index(params[1])
                                continente=0
                                for i in range(len(territories)):
                                    if indice>=len(territories[i]):
                                        indice-=len(territories[i])
                                        continente+=1
                                territories[continente][indice]=order.index(prossimo_giocatore)
                                if carta_territorio==False:
                                    while tris_usati[tris_cont]!=-1:
                                        tris_cont=(tris_cont+1)%len(tris_num)
                                    bot.sendMessage(idlist[order.index(prossimo_giocatore)],'Hai la nuova carta territorio '+territories_names[tris_num[tris_cont]]+' '+tris[tris_num[tris_cont]])
                                    tris_usati[tris_num[tris_cont]]=order.index(prossimo_giocatore)
                                    carta_territorio=True
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
        elif txt.startswith('Move') and idlist[order.index(prossimo_giocatore)]==chat_id:
            params=txt.split()[1:]
            if len(params)==3:
                if params[0] in territori_posseduti(order.index(prossimo_giocatore)):
                    if params[1] in territori_posseduti(order.index(prossimo_giocatore)):
                        if int(params[2])<truppe_terr[territories_names.index(params[1])]:
                            if borders[territories_names.index(params[0])][territories_names.index(params[1])]==1:
                                truppe_terr[territories_names.index(params[0])]-=params[2]
                                truppe_terr[territories_names.index(params[1])]+=params[2]
                                colora()
                                prossimo_giocatore=(prossimo_giocatore+1)%len(idlist)
                                rinforzo()
        elif txt.startswith('Fine') and idlist[order.index(prossimo_giocatore)]==chat_id:
            prossimo_giocatore=(prossimo_giocatore+1)%len(idlist)
            tris()

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    global wait
    if query_data == '/inizio' and wait:
        wait = False
        global idlist
        global order
        ordine_turni()
        dividi_territori()
        global truppe_disponibili
        for i in range(len(idlist)):
            bot.sendMessage(idlist[i], 'Lancio dei dadi per decidere chi inizia...\nYou\'re the player n.{}'.format(order[i]+1))
            bot.sendMessage(idlist[i], 'You have the following territories:'+territori_posseduti(i)+'\nAnd this goal: '+obiettivi(idlist[i]))
            bot.sendMessage(idlist[i], 'Hai a disposizione {} truppe, disponile nei tuoi territori scrivendo "Posiziona x1 x2 x3 ..." con x1, x2, x3, ... il numero di truppe da mettere in ogni territorio'.format(50-5*len(idlist)))
        colora()

bot=telepot.Bot('*INSERT YOUR TOKEN HERE*')
bot.message_loop({'chat': on_chat_message,'callback_query': on_callback_query})
print ('Listening ...')

while 1:
    time.sleep(10)
