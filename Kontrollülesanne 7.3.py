from easygui import * # EasyGui kasutamiseks importida
esimene = integerbox("Esimene täisarv", lowerbound = 1, upperbound = 10)
teine = integerbox("Teine täisarv", lowerbound = 1, upperbound = 10)
nupud = ["+","-","*"]
vajutati = buttonbox("Valige tehe ", choices = nupud)
if vajutati=="+":
    msgbox(str(esimene+teine))
elif vajutati=="-":
    msgbox(str(esimene-teine))
else:
    msgbox(str(esimene*teine))
