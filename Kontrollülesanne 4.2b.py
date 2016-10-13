from tkinter import *

raam = Tk()#loo raam

raam.title("Liiklusmärk")#raami pealkiri
tahvel = Canvas(raam,background='white', height=200, width=200)#tahvel raami sisse, valge
tahvel.create_oval(65,65,135,135, fill="white", outline="red",width=6)
tahvel.create_text(100,85,text="ERATEE")
tahvel.create_line(75,95, 125, 95,width=4)#joon kirja alla
tahvel.pack()#tahvel raamile
raam.mainloop()







