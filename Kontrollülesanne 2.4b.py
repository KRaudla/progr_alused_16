from random import randint
valik = input("Kas tahad ise valida kummal tribüünil istud 'ise' või see loositakse?")
if valik =="ise":
    valiktribüün= input("Kas põhjatribüün 'p' või lõunatribüün 'l' ?")
    if valiktribüün=="p":
        print ("Valisite ise. Pilet on põhjatribüünile")
    else:
        print ("Valisite ise. Pilet on lõunatribüünile")
else:
    rand= randint(1,3)
    if rand==1 or rand==2:
        print ("Pilet loositi. Pilet on põhjatribüünile.")
    else:
        print ("Pilet loositi. Pilet on lõunatribüünile.")