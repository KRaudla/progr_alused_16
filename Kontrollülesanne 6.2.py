def teleri_diagonaal(kaugus):
    diagonaal=round(kaugus* 100 * 0.39 / 2.5)
    return diagonaal
kaugus = float(input("Teleri kaugus meetrites on: "))

print (teleri_diagonaal(kaugus))