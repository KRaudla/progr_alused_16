nimi = input("Sisesta nimi: ")

if nimi[-2:] =="ne":
    print ("Abielus")
elif nimi[-2:] =="te":
    print ("Vallaline")
elif not nimi[-2:] =="ne" and nimi[-1:] =="e":
    print ("Määramata")
else:
    print ("Pole ilmselt leedulanna perekonnanimi")
