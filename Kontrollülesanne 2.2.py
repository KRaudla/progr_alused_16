pikkus = float(input("Sisesta pikkus :"))
kaelakaart = input("Kas omad kaelakaarti? ")
pilet = input("Kas omad piletit?")
if pikkus < 120 and (kaelakaart.lower() =="jah" or pilet.lower()=="jah"):
    print ("Pääseb")
else:
    print ("Ei pääse")