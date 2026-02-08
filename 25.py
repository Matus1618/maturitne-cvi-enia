import random

vstup = input("Zadaj svojich 6 tipov (čísla od 1 do 49 oddelené medzerou): ")
moje_tipy = []
for cislo in vstup.split():
    moje_tipy.append(int(cislo))

zrebovanie = []
while len(zrebovanie) < 6:
    nahodne = random.randint(1, 49)
    if nahodne not in zrebovanie:
        zrebovanie.append(nahodne)

print("Vyžrebované čísla:", zrebovanie)

moje_uhadnute = []
for cislo in moje_tipy:
    if cislo in zrebovanie:
        moje_uhadnute.append(cislo)

print("Moje uhádnuté čísla:", moje_uhadnute)
print("Počet mojich uhádnutých čísel:", len(moje_uhadnute))

pocty_vitazov = [0, 0, 0, 0, 0, 0, 0]

subor = open('loteria_1.txt', 'r')

for riadok in subor:
    tipy_ucastnika = []
    for c in riadok.split():
        tipy_ucastnika.append(int(c))
    
    uhadol_pocet = 0
    for cislo in tipy_ucastnika:
        if cislo in zrebovanie:
            uhadol_pocet = uhadol_pocet + 1
            
    pocty_vitazov[uhadol_pocet] = pocty_vitazov[uhadol_pocet] + 1

subor.close()

print("Práve 1 číslo uhádlo:", pocty_vitazov[1], "účastníkov")
print("Práve 2 čísla uhádlo:", pocty_vitazov[2], "účastníkov")
print("Práve 3 čísla uhádlo:", pocty_vitazov[3], "účastníkov")
print("Práve 5 čísel uhádlo:", pocty_vitazov[5], "účastníkov")
print("Práve 6 čísel uhádlo:", pocty_vitazov[6], "účastníkov")