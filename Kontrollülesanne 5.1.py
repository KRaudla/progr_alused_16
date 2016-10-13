kuu =int(input("Sisesta kuu: "))
registreeritud = [4, 22, 84, 130, 128, 108, 80, 59, 37, 19, 7, 7]
if kuu==0 or kuu>12:
    print ("Sisesta kuu number!1-jaanuar, 2-veebruar jne.")
else:
    print (str(kuu)+". kuul registreeriti "+str(registreeritud[kuu-1])+" uut mopeedi.")









