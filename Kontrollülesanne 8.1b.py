import requests
import json
#1. Programm,küsib kasutajalt aadressi.
#2. Päring tehakse maa-ameti serverisse
#3. Väljastatakse kasutajale aadressi asukoht koordinaatides (lng, lat) ja viide asukohale kaardil

#teisendan esialgu l-est97 koordinaatsüsteemi (aadress koordinaatideks). Töökindlam on kasutada maa-ameti vanemat teenust.
# võib ka kasutada http://geoportaal.maaamet.ee/est/Teenused/X-GIS-JSON-aadressiotsingu-teenuse-kirjeldus-p502.html
def geokodeeri(aadress):
    url = "http://inaadress.maaamet.ee/inaadress/gazetteer?address="+str(aadress)
    r = requests.get(url)
    j = r.content
    json_str = j.decode("utf-8")
    parsed_json = json.loads(json_str)
    #kui objekt 'addresses' on jsonis olemas, siis leidis koordinaadid
    if "addresses" in parsed_json:
       x = parsed_json["addresses"][0]["viitepunkt_x"]
       y = parsed_json["addresses"][0]["viitepunkt_y"]
       #kasuta järgmist funktsiooni, muutes leitud koordinaadid (l-est97) rahvusvahelisse formaati.
       uuedkoordinaadid(x,y)
    else:
        print ("Ei suuda kodeerida aadressi: "+str(aadress))
#võta l-est97 koordinaatsüsteemi punktid ja teisenda need rahvusvahelisse süsteemi.
def uuedkoordinaadid(x,y):
    url="http://www.maaamet.ee/rr/geo-lest/url/?xy="+x+","+y
    j = requests.get(url).content.decode("utf-8")
    Lat = j.split(",")[0]
    Lng =j.split(",")[1]
    print ("Lat: " +str(Lat)+" ja "+"Lng: "+str(Lng))
    print ("Asukoht kaardil: "+"http://geoportaal.maaamet.ee/url/xgis-latlon.php?lat="+str(Lat)+"&lon="+str(Lng)+"&out=xgis")

aadress = str(input("Sisesta aadress, mida soovid kodeerida: "))
geokodeeri(aadress)