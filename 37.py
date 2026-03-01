subor = open("hlasovanie_1.txt", "r", encoding="utf-8")
riadky = subor.readlines()
subor.close()
sms = len(riadky)
print("Celkovy pocet sm:", sms)
sutaziaci = []

for i in range(5220, 5230):
    sutaziaci.append(str(i))
for cislo_s in sutaziaci:
    suboru = cislo_s + ".txt"
    vystup = open(suboru, "w", encoding="utf-8")
    poradie = 1
    for riadok in riadky:
        tel = riadok.strip()
        if tel == cislo_s:
            vystup.write(str(poradie) + "\n")
        poradie = poradie + 1
    vystup.close()