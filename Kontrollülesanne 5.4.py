failinimi =str(input("Sisesta faili nimi: "))
with open(failinimi,"r",encoding="utf-8") as input_file:
    jrknr=1
    sihtkohad = []
    for line in input_file:
        sihtkoht = str(line.strip("\n"))
        print (str(jrknr)+" "+sihtkoht)
        sihtkohad.append(sihtkoht)
        jrknr=jrknr+1
    sihtkohanr=int(input("Valige mitmes sihtkoht broneerida: "))
    print("Reis on broneeritud. Sihtkoht on "+sihtkohad[sihtkohanr-1])



