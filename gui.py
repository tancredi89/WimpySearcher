from tkinter import *
import time
##Fix wimpy az generation! Az is the first line available in the wimpy for cda
##Fix parsing of wimpys after the window is loaded

window = Tk()
window.title("Wimpy Searcher")
window.configure(background = "dark grey")
window.geometry("350x300+500+300")


def click():
    global loaded
    if loaded == False:
        
        metop = metopEntry.get() # collect input from textbox
        orbit = orbitEntry.get() 
        if metop[-1] != '1' and metop[-1] != '2' and metop[-1] != '3':
            output.delete(0.0,END)
            output.insert(0.0, "Metop not entered correctly")
        else:
            from main import passes
            global passes
            output.delete(0.0,END)
            number = int(metop[-1])
            counter = float(5.0)
            try:
                loaded = True
                for p in passes[number-1]:
                    if orbit in p:
                        if 'Az' in p:
                            counter = 1.0
                        elif 'AOS5' in p:
                            counter = 3.0
                        elif 'LOS5' in p:
                            counter = 4.0
                        elif 'AOS' in p:
                            counter = 2.0
                        elif 'LOS' in p:
                            counter = 5.0
                        textOutput = str(p)+" "+str(passes[number-1][p]+'\n')
                        output.insert(counter,textOutput)
            except:
                output.delete(0.0,END)
                output.insert(0.0,"Wimpys were not found or loaded!")
    else:
        metop = metopEntry.get() # collect input from textbox
        orbit = orbitEntry.get()
        if metop[-1] != '1' and metop[-1] != '2' and metop[-1] != '3':
            output.delete(0.0,END)
            output.insert(0.0, "Metop not entered correctly")
        else: 
            output.delete(0.0,END)
            number = int(metop[-1])
            counter = float(5.0)
            for p in passes[number-1]:
                if orbit in p:
                    if 'Az' in p:
                        counter = 1.0
                    elif 'AOS5' in p:
                        counter = 3.0
                    elif 'LOS5' in p:
                        counter = 4.0
                    elif 'AOS' in p:
                        counter = 2.0
                    elif 'LOS' in p:
                        counter = 5.0
                    textOutput = str(p)+" "+str(passes[number-1][p]+'\n')
                    output.insert(counter,textOutput)
                else:
                    output.delete(0.0,END)
                    output.insert(0.0,"Metop pass not found")


# Title
Label(window, text="Wimpy Searcher", bg="dark grey", fg="black", font="none 20 bold").grid(row=0)
loaded = False

# User Inputs
Label(window, text="Metop [M0x]: ", bg="dark grey", fg="black", font="none 14") .place(x= 10, y = 40)
metopEntry = Entry(window, width=15, bg="white")
metopEntry.place(x=180, y=40)

Label(window, text="Orbit Number: ", bg="dark grey", fg="black", font="none 14") .place(x = 10, y = 80)
orbitEntry = Entry(window, width=15, bg="white")
orbitEntry.place(x=180, y=80)


# Button
Button(window, text = "Search", width = 6, command = click,bg="red", fg="black").place(x=200, y=110)


# Result section
Label (window, text="\nResult: ", bg="dark grey", fg="black", font="none 14") .place(x=20 ,y=120)
output = Text(window, width=75,height=6, wrap=WORD,background="white")
output.place(x=20,y=170, width=300)
output.insert(0.0,"Wimpys will be loaded after first search. Waiting to load Wimpys...")
window.mainloop()