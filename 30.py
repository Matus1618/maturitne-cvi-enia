import tkinter

canvas = tkinter.Canvas(width=650, height=200)
canvas.pack()

def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')

pocet = 15
hrac = 1

def kresli():
    canvas.delete('all')
    canvas.create_text(325, 20, text="ťahá hráč: " + str(hrac))
    canvas.create_text(325, 40, text="počet zápaliek: " + str(pocet))
    for i in range(pocet):
        zapalka(50 + i * 40, 70)

def stlacenie_klavesu(event):
    global pocet, hrac
    
    if event.char in ['1', '2', '3']:
        odoberame = int(event.char)
        
        if odoberame <= pocet:
            pocet = pocet - odoberame
            
            if pocet == 0:
                kresli()
                canvas.create_text(325, 180, text="Hráč " + str(hrac) + " vyhráva! Gratulujem!", fill="red")
            else:
                if hrac == 1:
                    hrac = 2
                else:
                    hrac = 1
                kresli()

kresli()
canvas.bind_all('<Key>', stlacenie_klavesu)
canvas.mainloop()