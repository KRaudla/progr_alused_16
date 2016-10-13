def kuu_nimi(kuunumber):
    kuu_nimed=["jaanuar","veebruar","märts","aprill","mai","juuni",\
               "juuli","august","september","oktoober","november","detsember"]
    return kuu_nimed[kuunumber-1]

def kuupäev_sõnena(kuupäev):
    kuu=kuupäev[3:5].lstrip('0')
    return kuupäev[:3]+" "+str(kuu_nimi(int(kuu)))+" "+kuupäev[-4:]+". a"

kuupäev=str(input("Sisesta kuupäev formaadis 'dd.mm.yyyy': "))
print (kuupäev_sõnena(kuupäev))



