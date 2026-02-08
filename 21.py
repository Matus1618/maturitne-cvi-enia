from random import*

vstup = open("poprehadzovany_text1_vstup.txt","r")
text=[]
for riadok in vstup:
    text.append(riadok.strip().split())
vstup.close()

vystup =""
for riadok in text:
    for word in riadok:
        newword = list(word[1:-1])
        shuffle(newword)
        newword = word[0] + "".join(newword) + word[-1]
        vystup = vystup + newword + " "
    vystup = vystup + "\n"
print(vystup)

vystupT = open("poprehadzovany_text1_vystup.txt","w")
vystupT.write(str(vystup))
vystupT.close()