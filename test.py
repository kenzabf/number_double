from tkinter import* 

def action():
    N = int(entryNumber_one.get())
    N2 = 2*N
    entryNumber_doub.delete(0,END)
    entryNumber_doub.insert(0 , N2)
doub = Tk()
doub.geometry("400x300")

number_one = Label(doub, text= "Entrer la valeur de N")
number_one.place(x = 50 , y= 50)
entryNumber_one = Entry(doub)
entryNumber_one.place(x = 200, y = 50) 


number_doub = Label(doub, text= "le double de N :")
number_doub.place(x = 50 , y= 100)
entryNumber_doub = Entry(doub)
entryNumber_doub.place(x = 200 , y = 100) 

calculer = Button(doub , text= "calculer l'operation " ,command= action)
calculer.place( x= 200 , y = 150 )


doub.mainloop()