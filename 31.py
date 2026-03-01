import tkinter
subor = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8")
rozmery = subor.readline()
rozmery1 = rozmery.strip().split()
riadky = subor.readlines()
sirka = int(rozmery1[0])
vyska = int(rozmery1[1])
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()

y = 0
for riadok in riadky:
    x = 0
    for farba in range(0, len(riadok.strip()),2):
        hex_f = riadok[farba:farba+2]
        tk_f = f"#{hex_f}{hex_f}{hex_f}"
        canvas.create_rectangle(x, y, x+1, y+1, fill=tk_f, outline=tk_f)
        x += 1
    y += 1

def button_1():
    y1 = 0
    for riadok in riadky:
        x1 = 0
        for farba in range(0, len(riadok.strip()),2):
            hex_f2 =  riadok[farba:farba+2]
            tk_f2  = int(hex_f2, 16)
            if tk_f2 < 128:
                canvas.create_rectangle(x1,y1,x1+1,y1+1, fill="black", outline="black")
            else:
                canvas.create_rectangle(x1,y1,x1+1,y1+1, fill="white", outline="white")
            x1 += 1
        y1 += 1
    print("zemnené")

button = tkinter.Button(text="Prepnúť", command=button_1)
button.pack()
canvas.mainloop()