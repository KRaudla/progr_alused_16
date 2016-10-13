inimestearv= int(input("inimeste arv"))
kohtadearv=int(input("kohtade arv"))

if kohtadearv>inimestearv:
    print ("Busse vaja: 1")
    print ("Viimases bussis inimesi: "+str(inimestearv))
else:
    üle = inimestearv%kohtadearv
    if üle>0:
        busse = (inimestearv//kohtadearv)+1
        print ("Busse vaja: "+str(busse))
        print ("Viimases bussis inimesi: "+str(üle))
    elif üle==0:
        busse = (inimestearv//kohtadearv)
        print ("Busse vaja: "+str(busse))
        print ("Viimases bussis inimesi: "+str(kohtadearv))
    else:
        busse = (inimestearv//kohtadearv)
        print ("Busse vaja: "+str(busse))
        print ("Viimases bussis inimesi: "+str(inimestearv))
