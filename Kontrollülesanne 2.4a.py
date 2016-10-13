vanus = int(input("Sisesta vanus: "))
sugu = input("Sisesta sugu: ")
tyyp = input("Sisesta treeningutüüp: ")

maxmees=220-vanus
maxnaine=206-(0.88*vanus)

if sugu.lower() =="n" and tyyp=="1":
    print ("Pulsisagedus peaks olema vahemiku "+str(round(0.5*maxnaine))+" kuni "+str(round(0.7*maxnaine)))
elif sugu.lower() =="n" and tyyp=="2":
    print ("Pulsisagedus peaks olema vahemiku "+str(round(0.7*maxnaine))+" kuni "+str(round(0.8*maxnaine)))
elif sugu.lower() =="n" and tyyp=="3":
    print ("Pulsisagedus peaks olema vahemiku "+str(round(0.8*maxnaine))+" kuni "+str(round(0.87*maxnaine)))
elif sugu.lower() =="m" and tyyp=="1":
    print ("Pulsisagedus peaks olema vahemiku "+str(round(0.5*maxmees))+" kuni "+str(round(0.7*maxmees)))
elif sugu.lower() =="m" and tyyp=="2":
    print ("Pulsisagedus peaks olema vahemiku "+str(round(0.7*maxmees))+" kuni "+str(round(0.8*maxmees)))
elif sugu.lower() =="m" and tyyp=="3":
    print ("Pulsisagedus peaks olema vahemiku "+str(round(0.8*maxmees))+" kuni "+str(round(0.87*maxmees)))