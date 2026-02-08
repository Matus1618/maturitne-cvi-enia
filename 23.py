vstup = open('vstupny_text.txt', 'r', encoding='utf-8')
vystup = open('zasifrovany_text_1.txt', 'w', encoding='utf-8')

kluc = input("Zadaj šifrovací kľúč (malé písmená): ")
akcia = input("Chceš šifrovať (s) alebo dešifrovať (d)? ")

abeceda = "abcdefghijklmnopqrstuvwxyz"

for riadok in vstup:
    zasifrovany_riadok = ""
    index_v_kluci = 0
    
    for znak in riadok:
        if znak in abeceda:
            pozicia_znaku = abeceda.find(znak)
            
            znak_kluca = kluc[index_v_kluci % len(kluc)]
            posun = abeceda.find(znak_kluca)
            
            if akcia == "s":
                nova_pozicia = (pozicia_znaku + posun) % 26
            else:
                nova_pozicia = (pozicia_znaku - posun) % 26
            
            zasifrovany_riadok = zasifrovany_riadok + abeceda[nova_pozicia]
            index_v_kluci = index_v_kluci + 1
        else:
            zasifrovany_riadok = zasifrovany_riadok + znak
            
    vystup.write(zasifrovany_riadok)

vstup.close()
vystup.close()