subor = open("dekompresia_obrazka_1.txt", "r", encoding="utf-8")
subor1 = open("dekompresia_obrazka_vystup.txt", "w", encoding="utf-8")

rozmery = subor.readline()
rozmery1 = rozmery.strip().split()
sirka = int(rozmery1[0])
vyska = int(rozmery1[1])

print("šírka:", sirka, "výška:", vyska, "Počet všetkých bodov:", sirka * vyska)

subor1.write(str(sirka) + " " + str(vyska) + "\n")
def spracuj_riadok(cisla_riadku):
    finalne_riadko = ""
    casti = cisla_riadku.strip().split()
    farba = "0"
    for cislo in casti:
        pocet = int(cislo)
        finalne_riadko = finalne_riadko + (farba * pocet)
        if farba == "0":
            farba = "1"
        else:
            farba = "0"
    return finalne_riadko


for riadok in subor:
    novy = spracuj_riadok(riadok)
    subor1.write(novy + "\n")

subor.close()
subor1.close()