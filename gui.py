from tkinter import *
from main import passes

##Fix wimpy az generation! Az is the first line available in the wimpy for cda
##Fix parsing of wimpys after the window is loaded


window = Tk()
window.title("Wimpy Searcher")
window.configure(background = "dark grey")
window.geometry("700x500+500+300")


def click():
    metop = metopEntry.get() # collect input from textbox
    orbit = orbitEntry.get() 
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


# Title
Label(window, text="Wimpy Searcher", bg="dark grey", fg="black", font="none 20 bold").grid(row=0, column=0,sticky=W)

# User Inputs
Label(window, text="Metop [M0x]: ", bg="dark grey", fg="black", font="none 14") .grid(row=1, column=0, sticky=W)
metopEntry = Entry(window, width=15, bg="white")
metopEntry .grid(row=1, column=0, sticky=E)

Label(window, text="Orbit Number: ", bg="dark grey", fg="black", font="none 14") .grid(row=2, column=0, sticky=W)
orbitEntry = Entry(window, width=15, bg="white")
orbitEntry .grid(row=2, column=0, sticky=E)


# Button
Button(window, text = "Search", width = 6, command = click,bg="white").grid(row=2, column=100, sticky=E)

# Result section
Label (window, text="\nResult: ", bg="dark grey", fg="black", font="none 14") . grid(row= 6, column = 0,sticky=W)
output = Text(window, width=75,height=6, wrap=WORD,background="white")
output.grid(row=7, column=0,columnspan=2,sticky=W)
window.mainloop()