# Import Module
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import img2pdf

# Create Object
root = Tk()

#personnaliser la fenetre
root.title("IMG2PDF par fabgth")
#root.iconbitmap("logo.ico")

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='IMG2PDF', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)



def select_file():
    global file_names
    file_names = askopenfilenames(initialdir="/", title="select_file")

browseButton = tk.Button(text="Selectionner des images", command=select_file, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)

#IMAGES TO PDF
#ajout fonction asksaveasfilename
def images_to_pdf():
    global nom
    nom= asksaveasfilename(initialdir="/", title="images_to_pdf")
    with open(nom+".pdf", "wb") as f:
        nom = f.write(img2pdf.convert(file_names))


# Bouton convert to pdf
saveAsButton = tk.Button(text='Convertir en PDF', command=images_to_pdf, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)



def exitApplication():
    MsgBox = tk.messagebox.askquestion('Quitter Application', "Voulez vous vraiment quitter l'application?", icon='warning')
    if MsgBox == 'oui':
        root.destroy()

# Bouton quitter
exitButton = tk.Button(root, text='      Quitter      ', command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

# Execute Tkinter
root.mainloop()
