def tervitus():

    print ('Võõrustaja: "Tere!"')
    print ('Külaline: "Tere, suur tänu kutse eest!"')

arv = int(input("Sisesta külaliste arv: "))
for i in range(1,arv+1):
    tervitus()