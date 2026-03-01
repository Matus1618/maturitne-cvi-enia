import tkinter
subor = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8")

rozmery = subor.readline()
rozmery1 = rozmery.strip().split()
riadky = subor.readlines()
sirka = int(rozmery1[0])
vyska = int(rozmery1[1])

canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()

pocet = [0] * 256

for riadok in riadky:
    rozdelenie = riadok.strip()
    for farba in range(0, len(rozdelenie), 2):
        hex_f = rozdelenie[farba:farba+2]
        farba_pocet =  int(hex_f, 16)
        pocet[farba_pocet] += 1

max_pocet = max(pocet)
mierka = 200 / max_pocet
x = -250
for i in range(256):
    stlpec = pocet[i] * mierka
    canvas.create_line(x, 500, x, 500 - stlpec, width=2, fill="gray")
    x += 2

print(pocet)
canvas.mainloop()