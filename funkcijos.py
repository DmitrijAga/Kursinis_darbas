import logging
from tkinter import messagebox
from tkinter import *


def info_message():
    logger.warning(f"Programos Info kvietimas")
    messagebox.showinfo('Info', 'Pirma mano paruošta programa\n Autorius Dmitrij Agafonov \n 2022 Lapkritis, Vilnius')


def iseiti():
    logger.warning(f"Programos išjungimas per meniu")
    quit()


def logu_skaitymas():
    logger.warning(f"Atidarė Log submeniu skirtukas")
    langas1 = Toplevel()
    langas1.title('Paskutiniai įrašai')
    langas1.geometry('900x400')
    with open("Savologas.log", "r", ) as failas, open("Readme.txt", "w",
                                                      encoding="UTF-8") as readme:  # išsiaiškinti koduotę
        tekstas = failas.read()
        readme.write(tekstas)

    sbar = Scrollbar(langas1, orient=VERTICAL)
    sbar.pack(side=RIGHT, fill='y')
    label4 = Text(langas1, yscrollcommand=sbar.set)
    label4.insert('1.0', tekstas)
    sbar.config(command=label4.yview)
    label4.place(relx=0, y=0, anchor=NW, relheight=1.0, relwidth=1.0)
    return tekstas


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("Savologas.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")  # arba UTF-8
file_handler.setFormatter(formatter)
