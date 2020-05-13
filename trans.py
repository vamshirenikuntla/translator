import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("translator")
win.geometry("200x70")


def translator():
    word = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word, dest="es")
    label1 = tk.Label(
        win, text=f'translated word : {translation.text}', bg="yellow")
    label1.grid(row=2, column=0)


label1 = tk.Label(win, text="write Here :")
label1.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

button = tk.Button(win, text="Go", command=translator)
button.grid(row=1, column=1)

win.mainloop()
