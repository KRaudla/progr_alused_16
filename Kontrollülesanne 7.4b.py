from urllib.request import urlopen

kuu = str(input("Kuu nimi: "))
päev =int(input("Päev: "))
failVeebis = urlopen("https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/"+kuu)
baidid = failVeebis.read()
tekst = baidid.decode() # baitidest saab sõne
ridadeKaupa = tekst.splitlines() # sõne jaotatakse reavahetuse kohtadelt
failVeebis.close()
print(ridadeKaupa[päev-1]) # rida indeksiga 4