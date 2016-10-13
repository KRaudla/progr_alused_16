filename = str(input("Sisesta failinimi: "))
with open(filename,"r") as inputfile:
    string = inputfile.read().upper()
    new = string.replace("Ä","AE").replace("Õ","OE").replace("Ö","OE").replace("Ü","UE")
    print (new)
