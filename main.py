from random import choice, sample
from tkinter import *
from tkinter import messagebox
import logging
from PIL import ImageTk, Image
from funkcijos import info_message, iseiti, logu_skaitymas



langas = Tk()
langas.title('Lietuvos miestai')
langas.geometry('900x600')
img = ImageTk.PhotoImage(Image.open("zemelapisPS.jpg"))
panel = Label(langas, image=img)
panel.pack(side="top", fill="both")
langas.resizable(width=False, height=False)



meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

#
# def info_message():
#     logger.warning(f"Programos Info kvietimas")
#     messagebox.showinfo('Info', 'Pirma mano paruošta programa\n Autorius Dmitrij Agafonov \n 2022 Lapkritis, Vilnius')


# def iseiti():
#     logger.warning(f"Programos išjungimas per meniu")
#     quit()


def start():
    global word, guessEntry, wordMix
    btnYes.place_forget()
    btnNo.place_forget()
    mygtukas['text'] = 'Patikrinti'
    langas.bind("<Return>", lambda event: check())
    mygtukas['width'] = 10
    mygtukas['command'] = check
    mygtukas.place(relx=0.5, y=300, anchor=CENTER)
    zodziu_ikelimas()
    word = choice(words)
    print(word)
    wordMix = sample(word, k=len(word))
    logger.info(f"Užduoties žodis:  {wordMix}")
    label1['text'] = 'Koks miestas čia užkoduotas?: '
    label2['text'] = ''.join(wordMix)
    guessEntry = Entry(langas, font='Arial 15 bold')
    guessEntry.place(relx=0.5, y=260, anchor=CENTER)
    status["text"] = "Įveskite žodį"


def zodziu_ikelimas():
    global words
    failas = open("zodziai.txt", "r", encoding="utf-8")
    data = failas.read()
    words = data.split("\n")
    logger.warning(f"Žodzių sarašas įkeltas")
    print(words)


def check():
    guess = guessEntry.get()
    logger.info(f"Ivestas variantas:  {guess}")
    if guess == word:
        guessEntry.place_forget()
        mygtukas.place_forget()
        label1['text'] = 'Jus atspėjote!'
        label2['text'] = 'Gal dar kartą?'
        label3['text'] = ''
        btnYes.place(x=350, y=280)
        btnNo.place(x=450, y=280)
        status["text"] = "Geras rezultatas"
        logger.info(f"Sekmingas bandymas")

    else:
        guessEntry.delete(0, 'end')
        label1['text'] = 'Jus neatspėjote, bandykite dar kartą'
        label2['text'] = 'Ar nepamiršai, kad miesto pavadinimas rašomas iš Didžiosios?'
        label3["text"] = 'Tai koks čia yra miestas?: ' + ''.join(wordMix)
        status["text"] = "Kaškas negerai"
        logger.info(f"Nesekmingas bandymas")


# def logu_skaitymas():
#     logger.warning(f"Atidarė Log submeniu skirtukas")
#     langas1 = Toplevel()
#     langas1.title('Paskutiniai įrašai')
#     langas1.geometry('400x400')
#     with open("Savologas.log", "r", ) as failas, open("Readme.txt", "w", encoding="UTF-8") as readme:
#         tekstas = failas.read()
#         readme.write(tekstas.upper())
#         print(tekstas)
#     with open("Savologas.log", "r", ) as failas, open("Readme.txt", "w",
#                                                       encoding="UTF-8") as readme:  # išsiaiškinti koduotę
#         tekstas = failas.read()
#         readme.write(tekstas)
#         print(tekstas)
#     label4 = Label(langas1, text=tekstas, font='Colibri 10')
#     label4.place(relx=0, y=0, anchor=W)
#     scrollbaras = Scrollbar(langas1)
#     boksas = Listbox(langas1, yscrollcommand=scrollbaras.set)
#     scrollbaras.config(command=boksas.yview)
#     boksas.insert(END, *tekstas)
#     scrollbaras.place(anchor=E)
#     boksas.place()
#     return tekstas



def exitGame():
    answer = messagebox.askokcancel('Išeiti', 'Ar tikrai norite išeiti?')
    if answer:
        logger.warning(f"Programa išjungta")
        langas.destroy()



logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("Savologas.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")  # arba UTF-8
file_handler.setFormatter(formatter)
logger.warning(f"Darbo pradžia")

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label='Log failas', command=logu_skaitymas)
submeniu.add_command(label="Apie programą", command=info_message)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)

words = []

label1 = Label(langas, text='Ar atspėsi Lietuvos miestų pavadinimus?', font='Arial 20 bold')
label2 = Label(langas, text='', font='Arial 15 italic')
label3 = Label(langas, text='', font='Arial 15 bold')


label1.place(relx=0.5, y=140, anchor=CENTER)
label2.place(relx=0.5, y=180, anchor=CENTER)
label3.place(relx=0.5, y=220, anchor=CENTER)

mygtukas = Button(langas, text='Pradėti', font='Arial 15 bold', width=20, command=start)
langas.bind("<Return>", lambda event: start())
mygtukas.place(relx=0.5, y=300, anchor=CENTER)
status = Label(langas, text="Sveiki, mes pradedam?", bd=1, relief=SUNKEN, anchor=W)
status.place(relx=0.0, y=580,relwidth=900)



btnYes = Button(langas, text='Taip', font='Arial 15 bold', width=5, command=start)
btnNo = Button(langas, text='Ne', font='Arial 15 bold', width=5, command=exitGame)

langas.mainloop()
