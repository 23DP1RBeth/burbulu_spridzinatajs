from tkinter import *

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
        a.move(kuga_id, 0, -KUGA_ATR)
    elif notikums.keysym == "Down":
        a.move(kuga_id, 0, -KUGA_ATR)
        a.move(kuga_id, 0, -KUGA_ATR)
    elif notikums.keysym == "Left":
        a.move(kuga_id, 0, -KUGA_ATR)
        a.move(kuga_id, 0, -KUGA_ATR)
    elif notikums.keysym == "Right":
        a.move(kuga_id, 0, -KUGA_ATR)
        a.move(kuga_id, 0, -KUGA_ATR)

a.bind_all('<Key>', parvietot_kugi)

input()
