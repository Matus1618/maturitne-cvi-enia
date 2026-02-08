import random

def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)

vstup = open('poprehadzovany_text_vstup2.txt', 'r', encoding='utf-8')
vystup = open('poprehadzovany_text.txt', 'w', encoding='utf-8')

for riadok in vstup:
    slova = riadok.split()
    novy_riadok = ""

    for slovo in slova:
        zaciatok = ""
        stred = ""
        koniec = ""
        
        while len(slovo) > 0 and not slovo[0].isalpha():
            zaciatok = zaciatok + slovo[0]
            slovo = slovo[1:]
            
        while len(slovo) > 0 and not slovo[-1].isalpha():
            koniec = slovo[-1] + koniec
            slovo = slovo[:-1]

        if len(slovo) > 3:
            prve = slovo[0]
            posledne = slovo[-1]
            stred = pomiesaj(slovo[1:-1])
            nove_slovo = zaciatok + prve + stred + posledne + koniec
        else:
            nove_slovo = zaciatok + slovo + koniec
            
        novy_riadok = novy_riadok + nove_slovo + " "

    vysledok = novy_riadok.strip()
    vystup.write(vysledok + "\n")

vstup.close()
vystup.close()