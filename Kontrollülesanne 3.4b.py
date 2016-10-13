from random import randint

arv = int(input("Sisestage visketabavuse protsent: "))
i=0
tabas = 0
while i<1000:
    i=i+1
    juhus = randint(1,100)
    if juhus>0and juhus<arv+1:
        print (str(i)+". vise tabas")
        tabas=tabas+1
    else:
        print (str(i)+". vise mööda")
print ("Tabas "+str(tabas)+" viset.")












