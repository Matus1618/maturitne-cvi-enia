import random

vstup = open('virus.txt', 'r', encoding='utf-8')
riadky = vstup.readlines()
vstup.close()

for r in riadky:
    print(r.strip())

if random.randint(1, 2) == 1:
    random.shuffle(riadky)

vystupny_text = []

for riadok in riadky:
    slova = riadok.split()
    
    if random.randint(1, 2) == 1:
        random.shuffle(slova)
    
    nove_slova = []
    for slovo in slova:
        if random.randint(1, 2) == 1:
            otocene = ""
            for i in range(len(slovo) - 1, -1, -1):
                otocene = otocene + slovo[i]
            nove_slova.append(otocene)
        else:
            nove_slova.append(slovo)
    
    vysledny_riadok = ""
    for s in nove_slova:
        vysledny_riadok = vysledny_riadok + s + " "
    
    vystupny_text.append(vysledny_riadok.strip())

vystup = open('virus_vystup.txt', 'w', encoding='utf-8')
for riadok in vystupny_text:
    print(riadok)
    vystup.write(riadok + "\n")
vystup.close()