# Fenetre
import tkinter
from tkinter.messagebox import *

def verification ():
	# si le mot correspond à celui attendu
	if var_entry1.get() == 'toto': 
		showinfo('Résultat','Mot de passe correct.\nAu revoir !')
	else:
		showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
		var_entry1.set('')

	
root = tkinter.Tk()
root.geometry("400x400")
root.title("Mon TP A RENDRE ")

mainmenu = tkinter.Menu(root)

w = tkinter.Label(root, text = "Veuillez saisir vos informations!")
#Zone de Saisie
var_entry1 = tkinter.StringVar()
entry1 = tkinter.Entry(root,textvariable=var_entry1)
var_entry2 = tkinter.StringVar()

entry2 = tkinter.Entry(root,textvariable=var_entry2)

# Bouton
bouton = tkinter.Button(root,text='Connexion', command=verification)
var_gender = tkinter.IntVar()

w.pack()
entry1.pack()
entry2.pack()
bouton.pack()
root.config(menu=mainmenu)
root.mainloop()