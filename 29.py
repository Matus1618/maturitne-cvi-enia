def spracuj_riadok(riadok):
    riadok = riadok.strip()
    vysledok = []
    
    if riadok[0] == '1':
        vysledok.append(0)
    
    aktualny_znak = riadok[0]
    pocet = 0
    
    for znak in riadok:
        if znak == aktualny_znak:
            pocet = pocet + 1
        else:
            vysledok.append(pocet)
            aktualny_znak = znak
            pocet = 1
    vysledok.append(pocet)
    
    retazec = ""
    for cislo in vysledok:
        retazec = retazec + str(cislo) + " "
    return retazec.strip()

f_vstup = open('kompresia_obrazka_1.txt', 'r')
prvy_riadok = f_vstup.readline().split()
sirka = int(prvy_riadok[0])
vyska = int(prvy_riadok[1])

print("Sirka:", sirka)
print("Vyska:", vyska)
print("Pocet bodov:", sirka * vyska)

f_vystup = open('kompresia_obrazka_vystup.txt', 'w')
f_vystup.write(str(sirka) + " " + str(vyska) + "\n")

riadky = f_vstup.readlines()
f_vstup.close()

prvy_riadok_obr = riadky[0]
print(spracuj_riadok(prvy_riadok_obr))

for r in riadky:
    kompresia = spracuj_riadok(r)
    f_vystup.write(kompresia + "\n")

f_vystup.close()