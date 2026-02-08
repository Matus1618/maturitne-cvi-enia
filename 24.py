import random

vstupny_subor = open('vstupny_text.txt', 'r', encoding='utf-8')
vystupny_subor = open('zasifrovany_text_2.txt', 'w', encoding='utf-8')

akcia = input("Chceš šifrovať (s) alebo dešifrovať (d)? ")

abeceda = "abcdefghijklmnopqrstuvwxyz"

for riadok in vstupny_subor:
    if akcia == "s":
        posun = random.randint(1, 25)
        pismeno_posunu = abeceda[posun]
        
        novy_riadok = pismeno_posunu
        for znak in riadok:
            if znak in abeceda:
                index = abeceda.find(znak)
                nova_pozicia = (index + posun) % 26
                novy_riadok = novy_riadok + abeceda[nova_pozicia]
            else:
                novy_riadok = novy_riadok + znak
        
        print(novy_riadok, end="")
        vystupny_subor.write(novy_riadok)
        
    else:
        if len(riadok) > 0:
            pismeno_posunu = riadok[0]
            posun = abeceda.find(pismeno_posunu)
            zvysok_riadka = riadok[1:]
            
            novy_riadok = ""
            for znak in zvysok_riadka:
                if znak in abeceda:
                    index = abeceda.find(znak)
                    nova_pozicia = (index - posun) % 26
                    novy_riadok = novy_riadok + abeceda[nova_pozicia]
                else:
                    novy_riadok = novy_riadok + znak
            
            vystupny_subor.write(novy_riadok)

vstupny_subor.close()
vystupny_subor.close()