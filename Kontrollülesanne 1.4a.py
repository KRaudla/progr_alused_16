while True:
    try:
        ainepunktide_arv=int(input("Sisesta ainepunktide arv: "))
        nadalate_arv=int(input("Sisesta nädalate arv: "))
        ajakulu = ainepunktide_arv*26
        uhenadalaajakulu=round(ajakulu/nadalate_arv)
        print (uhenadalaajakulu)
    except ValueError:
        print ("Sisesta täisarv! Proovi uuesti.")
        continue
    else:
        break
