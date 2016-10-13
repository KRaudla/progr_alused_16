def pronksikarva_summa(inp):
    summa=0
    for i in inp:
        if i in (1,2,5):
            summa=summa+i
    return summa

filename=str(input("Sisesta faili nimi: "))
with open(filename,"r")as inp:
    mundid_list = []
    for i in inp:
        mundid_list.append(int(i.strip("\n")))
    summa = pronksikarva_summa(mundid_list)
    print ("Hoiupõrsasse läheb: "+str(summa)+" senti.")

