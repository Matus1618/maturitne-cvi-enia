subor = open("objednavanie_jedla.txt","r")
pocet = 0
z, c, m, o = 0, 0, 0, 0
for riadok in subor:
    pocet += 1
    riadok = riadok.strip()
    if subor[-1] == "z":
        z += 1
    elif subor[-1] == "c":
        c += 1
    elif riadok[-1] == "m":
        m += 1
    else:
        o += 1

print("Počet objednaných jedál:",pocet)
print("Zelene jedlo  bolo objednane: ",z," krát.")
print("Červene jedlo  bolo objednane: ",c," krát.")
print("Modre jedlo  bolo objednane: ",m," krát.")
print("Oranžové jedlo  bolo objednane: ",o," krát.")

if z < 20:
    print("Zelených jedál bolo menej ako 20.")
if c < 20:
    print("Červených jedál bolo menej ako 20.")
if m < 20:
    print("Modrích jedál bolo menej ako 20.")
if o < 20:
    print("Oranžových jedál bolo menej ako 20.")

subor.close()