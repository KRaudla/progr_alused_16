def eelarve(kutsutud):
    söök=kutsutud*10
    ruum=55
    return söök+ruum
kutsutud = int(input("Kutsutud külaliste arv on: "))
teatanud = int(input("Teatanud külaliste arv on: "))

print ("Maksimaalne eelarve on: "+str(eelarve(kutsutud))+" eurot")
print ("Minimaalne eelarve on: "+str(eelarve(teatanud))+" eurot")