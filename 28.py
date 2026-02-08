subor1 = open('hlasovanie_1.txt', 'r')
vsetky_hlasy = []
for riadok in subor1:
    vsetky_hlasy.append(riadok.strip())
subor1.close()

print("Celkovy pocet SMS:", len(vsetky_hlasy))

ucty = {}
for i in range(5220, 5230):
    c = str(i)
    ucty[c] = 0

for h in vsetky_hlasy:
    if h in ucty:
        ucty[h] = ucty[h] + 1

for k, v in ucty.items():
    print("Sutaziaci", k, "dostal", v, "hlasov")

min_hlasov = 999999
vypadava = ""
for k, v in ucty.items():
    if v < min_hlasov:
        min_hlasov = v
        vypadava = k

print("Najmenej hlasov (nepostupuje):", vypadava)

subor2 = open('hlasovanie_vypadnuti.txt', 'r')
vypadnuti = []
for riadok in subor2:
    vypadnuti.append(riadok.strip())
subor2.close()

min_hlasov2 = 999999
vypadava2 = ""
for k, v in ucty.items():
    if k not in vypadnuti:
        if v < min_hlasov2:
            min_hlasov2 = v
            vypadava2 = k

print("Najmenej hlasov bez vypadnutych:", vypadava2)