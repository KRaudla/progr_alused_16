#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))

with open("sunnikuupaevad.txt","r") as inputfile:
    for i in range(1,10):
        open("eluteenumber"+str(i)+".txt","a")
    for line in inputfile:
        nr =elutee(line.strip("\n"))
        outputfile = open("eluteenumber"+str(nr)+".txt","a")
        outputfile.write(line.strip("\n")+"\n")

