arv = int(input("Sisesta klientide arv: "))
summa=0
for i in range(1,arv+1):
    if i%2==1:
        summa=summa+i
    else:
        continue
print (summa)






