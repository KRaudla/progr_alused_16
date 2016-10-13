with open("konto.txt","r",encoding="utf-8") as input_file:
    for line in input_file:
        if float(line) >= 0:
           print (line.strip("\n"))


