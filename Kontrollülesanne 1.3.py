while True:
    try:
        astme_alus=int(input("Sisesta astme alus: "))
        aste=int(input("Sisesta aste: "))
        print (int(astme_alus**aste))
    except ValueError:
        print ("See pole täisarv! Proovi uuesti.")
        continue
    else:
        break
