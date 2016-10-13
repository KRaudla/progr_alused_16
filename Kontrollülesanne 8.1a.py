filename = str(input("Sisestage failinimi: "))
kmprotsent=int(input("Sisestage riigi käibemaks: "))
piirmäär=int(input("Sisesta summa, millest alates saad KM tagasi: "))
def hind_käibemaksuga(hind,määr):
    summa=0
    kmgaHind = hind * (1 + määr/100)
    summa=summa+kmgaHind
    return summa
with open(filename,"r",encoding="utf-8") as inputfile:
    summa=0
    summa2=0
    for line in inputfile:
        rida = line.strip("\n")
        summa=summa+hind_käibemaksuga(float(rida),kmprotsent)
        if hind_käibemaksuga(float(rida),kmprotsent)>piirmäär:
            summa2=summa2+hind_käibemaksuga(float(rida),kmprotsent)
    print("Kokku on kulutatud: "+str(round(summa,2)))
    print("Tagasi saab: "+str(round(summa2 - summa2/(1+kmprotsent/100),2)))