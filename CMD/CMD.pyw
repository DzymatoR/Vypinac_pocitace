import os
import datetime
from tkinter import *
from PIL import Image


tema = "dimgray"

okno = Tk()
# okno.minsize (219, 300)
okno.title ("Vypínač")
okno.config (bg = tema)
okno.resizable (False, False)

# funkce

def vypniMe():

    # příprava proměnných z Entry

    hodina = hodinEnt.get()
    minuta = minutEnt.get()
    sekunda = sekundEnt.get()
    kontrolka = check.get()

    ted = datetime.datetime.now()

    if kontrolka == 1:
        # výpočet zbývajícího času

        zbyvajiciCas = int(hodina) * 3600 + int(minuta) * 60 + int(sekunda)

        logoPopisek.configure(text = "Nastaveno", fg = "lightgreen")
        
        os.popen ("shutdown /s /f /t " + str(zbyvajiciCas))

    else: 
        
        zbyvajiciCas = (int(hodina) * 3600 + int(minuta) * 60 + int(sekunda)) - (int(ted.hour)*3600 + int(ted.minute)*60 + int(ted.second))

        logoPopisek.configure(text = "Nastaveno", fg = "lightgreen")

        os.popen ("shutdown /s /f /t " + str(zbyvajiciCas))
        


def zrusVypnuti():

    logoPopisek.configure(text = "Nenastaveno", fg = "red")
    
    os.popen ("shutdown /a")

    
def vynulujCitace():

    hodinEnt.delete(0,4)
    hodinEnt.insert (0, "0")

    minutEnt.delete(0,4)
    minutEnt.insert (0, "0")

    sekundEnt.delete(0,4)
    sekundEnt.insert (0, "0")


def casCitace():

    ted = datetime.datetime.now()


    hodinEnt.delete(0,4)
    hodinEnt.insert (0, ted.hour)

    minutEnt.delete(0,4)
    minutEnt.insert (0, ted.minute)

    sekundEnt.delete(0,4)
    sekundEnt.insert (0, ted.second)

   
#################
#               #
#  Tkinter GUI  #
#               #
#################


# pozicování obrázku

obrazek = Frame (okno, height = 100, bg = tema)
obrazek.grid()

Image.open("shutdown_img_blue.png").convert("RGBA")

logo = PhotoImage (file = "shutdown_img_blue.png")

logoLabel = Label(obrazek, image = logo, height = 150, borderwidth = 0, bg = tema)
logoLabel.grid(row = 0, sticky = W+E)

logoPopisek = Label(obrazek, text= "Nenastaveno", bg = tema, fg = "red", font = 25)
logoPopisek.grid(row = 1, sticky = W+E)

mezera = Frame(obrazek, height = 15, bg = tema)
mezera.grid(row = 2)


# pozicování čítačů

horni = Frame (okno, width = 250, height = 200, bg = tema, padx = 40)
horni.grid(row = 1, column = 0)


hodinEnt = Spinbox (horni, from_=0, to = 99, width = 5, justify = RIGHT)
# hodinEnt.insert (0,"0")
hodinEnt.grid(row = 0, column = 1)

minutEnt = Spinbox (horni, from_=0, to = 59, width = 5, justify = RIGHT)
# minutEnt.insert(0, "0")
minutEnt.grid(row = 0, column = 2)

sekundEnt = Spinbox (horni, from_=0, to = 59, width = 5, justify = RIGHT)
# sekundEnt.insert (0, "0")
sekundEnt.grid(row = 0, column = 3)

hodinLab = Label (horni, text = "hod.", bg = tema)
hodinLab.grid(row = 1, column = 1)

minutLab = Label (horni, text = "min.", bg = tema)
minutLab.grid(row = 1, column = 2)

sekundLab = Label (horni, text = "sec.", bg = tema)
sekundLab.grid(row = 1, column = 3)

check = IntVar()
check.set(1)

radioButton01 = Radiobutton(horni, text = "Vypnout za: ", variable = check, value = 1, bg = tema, command = vynulujCitace)
radioButton01.grid(row = 2, columnspan = 3, sticky = W)

radioButton02 = Radiobutton(horni, text = "Vypnout v: ", variable = check, value = 2, bg = tema, command = casCitace)
radioButton02.grid(row = 3, columnspan = 3, sticky = W)



# pozicování tlačítek

dolni = Frame (okno, width = 250, height = 100, bg = tema)
dolni.grid(row = 2, column = 0)

mezera = Frame(dolni, height = 20, bg = tema)
mezera.grid(row = 0)

vypni = Button (dolni, text = "Vypni!", width = 10, bg = "green", fg = "white", command = vypniMe)
vypni.grid(row = 1, sticky = W+E)

mezera = Frame(dolni, height = 10, bg = tema)
mezera.grid(row = 2)

zrus = Button (dolni, text = "Zruš vypnutí!", width = 20, bg = "red", fg = "white", command = zrusVypnuti)
zrus.grid(row = 3, sticky = W+E)

mezera = Frame(dolni, height = 20, bg = tema)
mezera.grid(row = 4)

# pozicování poznámek

kredit = Frame (okno, height = 100, bg = tema)
kredit.grid(row = 3, column = 0)

copyright = Label (kredit, text = "Džym 2018", bg = tema)
copyright.grid()


okno.mainloop()
