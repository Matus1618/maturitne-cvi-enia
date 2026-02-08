import tkinter
import random

canvas = tkinter.Canvas(width=800, height=500, bg='lightblue')
canvas.pack()

pocet = 5
for k in range(pocet):
    x_vrchol = random.randint(100, 700)
    y_vyska = random.randint(300, 450)
    typ = random.randint(1, 2)
    
    body = []
    body.append(0)
    body.append(500)
    body.append(0)
    body.append(y_vyska)
    
    for x in range(10, 810, 10):
        zmena = random.randint(0, 15)
        if typ == 1:
            if x < x_vrchol:
                y_vyska = y_vyska - zmena
            else:
                y_vyska = y_vyska + zmena
        else:
            if x < x_vrchol:
                y_vyska = y_vyska + zmena
            else:
                y_vyska = y_vyska - zmena
        
        body.append(x)
        body.append(y_vyska)
        
    body.append(800)
    body.append(500)
    
    zelena = random.randint(100, 200)
    farba = "#00" + hex(zelena)[2:] + "00"
    
    canvas.create_polygon(body, fill=farba, outline='black')

def nova_krajina(event):
    if event.keysym == 'space':
        canvas.delete('all')
        for k in range(5):
            x_vrchol = random.randint(100, 700)
            y_vyska = random.randint(300, 450)
            typ = random.randint(1, 2)
            body = [0, 500, 0, y_vyska]
            for x in range(10, 810, 10):
                zmena = random.randint(0, 15)
                if typ == 1:
                    if x < x_vrchol:
                        y_vyska = y_vyska - zmena
                    else:
                        y_vyska = y_vyska + zmena
                else:
                    if x < x_vrchol:
                        y_vyska = y_vyska + zmena
                    else:
                        y_vyska = y_vyska - zmena
                body.append(x)
                body.append(y_vyska)
            body.append(800)
            body.append(500)
            zelena = random.randint(100, 200)
            farba = "#00" + hex(zelena)[2:] + "00"
            canvas.create_polygon(body, fill=farba, outline='black')

canvas.bind_all('<Key>', nova_krajina)
tkinter.mainloop()