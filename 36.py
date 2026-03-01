import tkinter
def vykresli_krizovku(x_start, y_start, velkost, vyplnena):
    subor = open("krizovka2_1.txt", "r", encoding="utf-8")
    tajnicka = subor.readline().strip()
    slova = subor.readlines()
    subor.close()
    y = y_start
    for i in range(len(tajnicka)):
        slovo = slova[i].strip()
        p_tajnicky = tajnicka[i]
        pozicia = slovo.find(p_tajnicky)
        x = x_start - (pozicia * velkost)
        for j in range(len(slovo)):
            farba_pozadia = "white"
            if j == pozicia:
                farba_pozadia = "grey"
            canvas.create_rectangle(x, y, x + velkost, y + velkost, fill=farba_pozadia)
            if vyplnena == True:
                canvas.create_text(x + velkost//2, y + velkost//2, text=slovo[j], font = "Arial 15 bold")
            x = x + velkost
        y = y + velkost

canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()
vykresli_krizovku(150, 50, 30, False)
vykresli_krizovku(500, 50, 30, True)
canvas.mainloop()