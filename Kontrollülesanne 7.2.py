from datetime import datetime
kirje = str(input("Sisesta: "))
with open("paevik.txt","a") as outputfile:
    outputfile.write(str(datetime.today())+"\n")
    outputfile.write(kirje)
    outputfile.write("\n")