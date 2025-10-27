subor = open('hada.txt', 'r')
kopia = open('hada_kopia.txt', 'w')
pocet_hier = 0
najdlhsia = 0
znak1 = 'D'
pocet = 0

for riadok in subor:
    pocet_hier += 1
    if len(riadok) > najdlhsia:
        najdlhsia = len(riadok)
    for znak in riadok:
        if znak == znak1:
            pocet += 1
        else:
            if pocet != 0:
                kopia.write(str(pocet) + '-' + str(znak1) + ';')
            znak1 = znak
            pocet = 1
    kopia.write('\n')
    znak1 = 'D'
    pocet = 0

subor.close()
kopia.close()

print('Pocet hier zapisanych va subore je: ' + str(pocet_hier))
print('Najdlhsia hra ma ' + str(najdlhsia) + ' krokov.')

