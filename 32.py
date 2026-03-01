import tkinter
subor = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8")
subor1 = open("konverzia_suboru_1_vystup.txt", "w", encoding="utf-8")

rozmery = subor.readline()
rozmery1 = rozmery.strip().split()
riadky = subor.readlines()
sirka = int(rozmery1[0])
vyska = int(rozmery1[1])

canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()

def spracuj_riadok(zmena_riadky):
    subor1.write( str(sirka) + " " + str(vyska))
    for riadok in zmena_riadky:
        subor1.write("\n")
        for farba in range(0, len(riadok.strip()),2):
            hex_f = riadok[farba:farba+2]
            tk_f = int(hex_f, 16)
            if tk_f < 128:
                subor1.write(" " + "0")
            else:
                subor1.write(" " + "1")

spracuj_riadok(riadky)

subor1.close()