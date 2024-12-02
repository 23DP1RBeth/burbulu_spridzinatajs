from tkinter import *
from random import randint
from time import sleep, time

# 1 programma

GARUMS = 500
PLATUMS = 800

logs = Tk()
logs.title("Burbuļu spiridzinātājs")

a = Canvas(logs, width=PLATUMS, height=GARUMS, bg='darkblue')

a.pack()

# 2 programma

kuga_id = a.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
kuga_id2 = a.create_oval(0, 0, 30, 30, outline='red')

KUGA_R = 15
VID_X = PLATUMS / 2
VID_Y = GARUMS / 2

a.move(kuga_id, VID_X, VID_Y)
a.move(kuga_id2, VID_X, VID_Y)

# 3 programma

KUGA_ATR = 10
def parvietot_kugi(notikums):
    if notikums.keysym == 'Up':
        a.move(kuga_id, 0, -KUGA_ATR)
        a.move(kuga_id2, 0, -KUGA_ATR)
    elif notikums.keysym == "Down":
        a.move(kuga_id, 0, KUGA_ATR)
        a.move(kuga_id2, 0, KUGA_ATR)
    elif notikums.keysym == "Left":
        a.move(kuga_id, -KUGA_ATR, 0)
        a.move(kuga_id2, -KUGA_ATR, 0)
    elif notikums.keysym == "Right":
        a.move(kuga_id, KUGA_ATR, 0)
        a.move(kuga_id2, KUGA_ATR, 0)

a.bind_all('<Key>', parvietot_kugi)

# 4 programma

burb_id = list()
burb_r = list()

burb_atrums = list()

MIN_BURB_R = 10
MAX_BURB_R = 30
MAX_BURB_ATR = 10

ATSTARPE = 100
def izveidot_burbuli():
    x = PLATUMS + ATSTARPE
    y = randint(0, GARUMS)
    r = randint(MIN_BURB_R, MAX_BURB_R)
    id1 = a.create_oval(x - r, y - r, x + r, y + r, outline='white')

    burb_id.append(id1)
    burb_r.append(r)
    burb_atrums.append(randint(1, MAX_BURB_ATR))

# 5 programma

def parvietot_burbulus():
    for i in range(len(burb_id)):
        a.move(burb_id[i], -burb_atrums[i], 0)

# 7 programma
            
def iegut_koord(id_skaitlis):
    poz = a.coords(id_skaitlis)

    x = (poz[0] + poz[2]) / 2

    y = (poz[1] + poz[3]) / 2

    return x, y

# 8 programma

def dzest_burbuli(i):
    del burb_r[i]

    del burb_atrums[i]

    a.delete(burb_id[i])
    del burb_id[i]

# 9 programma

def notirit_burbulus():
    for i in range(len(burb_id) -1, -1, -1):
        x, y = iegut_koord(burb_id[i])
        if x < -ATSTARPE:
            dzest_burbuli(i)

# 11 programma
                
from math import sqrt

def attalums(id1, id2):
    x1, y1 = iegut_koord(id1)
    x2, y2 = iegut_koord(id2)

    return sqrt((x2 - x1) **2 + (y2 - y1) **2)

# 12 programma

def sadursme():

    punkti = 0
    for burb in range(len(burb_id)-1, -1, -1):
        if attalums(kuga_id2, burb_id[burb]) < (KUGA_R + burb_r[burb]):
            punkti += (burb_r[burb] + burb_atrums[burb])
            dzest_burbuli(burb)
    return punkti


a.create_text(50, 30, text='LAIKS', fill='white')
a.create_text(150, 30, text='REZULTĀTS', fill='white')

laiks_teksts = a.create_text(50, 50, fill='white')
rezultats_teksts = a.create_text(150, 50, fill='white')

def paradit_rezultatu(rezultats):
    a.itemconfig(rezultats_teksts, text=str(rezultats))

def paradit_laiku(laiks_palicis):
    a.itemconfig(laiks_teksts, text=str(laiks_palicis))
    
# 6 programma
        
BURB_NEJAUSI = 10
LAIKA_IEROBEZOJUMS = 30
PAPILDALAIKA_REZ = 1000

rezultats = 0

papildu = 0

beigas = time() + LAIKA_IEROBEZOJUMS

# SPĒLES GALVENAIS CIKLS

while time() < beigas:

    if randint(1, BURB_NEJAUSI) == 1:
        izveidot_burbuli()
    parvietot_burbulus()
    notirit_burbulus()
    rezultats += sadursme()
    if(int(rezultats / PAPILDALAIKA_REZ)) > papildu:
        papildu += 1
        beigas += LAIKA_IEROBEZOJUMS
    paradit_rezultatu(rezultats)
    paradit_laiku(int(beigas - time()))
    logs.update()
    sleep(0.01)

a.create_text(VID_X, VID_Y, \
    text='SPĒLES BEIGAS', fill='white', font=('Helvetica', 30))
a.create_text(VID_X, VID_Y + 30, \
    text='Rezultāts: ' + str(rezultats), fill='white')
a.create_text(VID_X, VID_Y + 45, \
    text='Papildu laiks: ' + str(papildu*LAIKA_IEROBEZOJUMS), fill='white')
    
input()

            
