käärikul = [401, 604, 547, 700, 722, 845, 621, 490, 800, 700]
kohilas = [900, 0, 333, 803, 838, 400, 467, 488, 432, 700]
kokku=0
parimad=[]
for f, b in zip(käärikul,kohilas):
    parim=max([f, b])
    parimad.append(parim)
    kokku=kokku+int(parim)
print (parimad)
print (kokku)




