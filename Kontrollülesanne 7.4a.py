def eelarve(kutsutud):
    söök=kutsutud*10
    ruum=55
    return söök+ruum
#kutsutud = int(input("Kutsutud külaliste arv on: "))
#teatanud = int(input("Teatanud külaliste arv on: "))

filename="külalised.txt"
with open(filename,"r") as inputfile:
    tulevad=0
    kokku =0
    for line in inputfile:
        kokku=kokku+1
        if line.strip("\n")[:1]=="+":
            tulevad=tulevad+1
    print ("kutsutud "+str(kokku))
    print("tulevad "+str(tulevad))
    print ("Max "+str(eelarve(kokku)))
    print("Min "+str(eelarve(tulevad)))


#print ("Maksimaalne eelarve on: "+str(eelarve(kutsutud))+" eurot")
#print ("Minimaalne eelarve on: "+str(eelarve(teatanud))+" eurot")