from datetime import *
fail = str(input("Sisesta failnimi: "))
with open(fail,"r") as input_file:
    for i, line in enumerate(input_file):
        rida = str(line.strip("\n"))
        if i+1 == int(datetime.now().day):
            print ("Vastama tuleb: " + str(rida))



