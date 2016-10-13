while True:
    try:
        nimi =str(input("Isiku nimi: "))
        lubatud_kiirus=int(input("Sisesta lubatud kiirus: "))
        tegelik_kiirus=int(input("Sisesta tegelik kiirus: "))
        trahv = (tegelik_kiirus-lubatud_kiirus)*3
        if trahv<0:
            print (nimi+", sa oled tubli. Sa ei ületanud kiirust.")
        elif trahv==0:
            print (nimi+", sinu kiirus oli täpselt lubatud sõidukiiruse piires"+" ("+str(lubatud_kiirus)+"km/h.)")
        elif trahv==1:
            print (nimi+", kiiruse ületamise eest on teie trahv "+str(trahv)+" euro.")
        elif trahv>0 and trahv<191:
            print (nimi+", kiiruse ületamise eest on teie trahv "+str(trahv)+" eurot.")
        elif trahv>=190:
            print (nimi+", kiiruse ületamise eest on teie trahv 190 eurot.")
        else:
            break
    except ValueError:
        print ("Sisesta täisarv! Proovi uuesti.")
        continue
    else:
        break
