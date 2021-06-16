from tkinter.messagebox import *
from tkinter import * 
from fonctions import btn_importer_click, btn_coder_click, btn_decoder_click, btn_exporter_click

#Initialisation de la fenetre
root = Tk()
root.title("Le chiffrage César")

#Definition de la taille de la fenetre
root.geometry("800x300")
root.minsize(800, 150)

#Definition des colonnes et lignes à étirer quand la taille de la fenetre change
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)




#Creation label input
lbl_input = Label(root, text="Entrer le texte à coder/décoder:")
lbl_input.grid(column=0, row=0, sticky='s')
#Creation de cadre d'input
txt_input = Text(root)
txt_input.grid(column=0, row=1, rowspan=2, sticky='nsew', padx=10, pady=10)

#Creation du bouton pour importer le contenu d'un fichier
btn_importer = Button(root, text="Importer", width=15, command= lambda: btn_importer_click(txt_input) )
btn_importer.grid(row=3, column=0)



#Creation du label pour la zone de texte du décalage
lbl_decalage = Label(root, text="Décalage:")
lbl_decalage.grid(column=0, row=3, sticky="e")
#Creation de la zone de texte du decalage
var_decalage = StringVar() 
var_decalage.set("8")
entry_decalage = Entry(root, textvariable=var_decalage)
entry_decalage.grid(column=1, row=3, sticky='nsew', padx=10, pady=10)



#Creation des boutons coder et décoder
btn_coder = Button(root, text="Coder le texte", width=15, command= lambda: btn_coder_click(txt_input, txt_output, var_decalage))
btn_coder.grid(row=1, column=1)
btn_decoder = Button(root, text="Décoder le texte", width=15, command= lambda: btn_decoder_click(txt_input, txt_output, var_decalage))
btn_decoder.grid(row=2, column=1)



#Creation label output
lbl_output = Label(root, text="Résultat:")
lbl_output.grid(column=2, row=0, sticky='s')
#Creation cadre output
txt_output = Text(root, state=DISABLED)
txt_output.grid(column=2, row=1, rowspan=2, sticky='nsew', padx=10, pady=10)

#Creation du bouton pour exporter le resultat dans un fichier
btn_exporter = Button(root, text="Exporter", width=15, command= lambda: btn_exporter_click(txt_output) )
btn_exporter.grid(row=3, column=2)



#Creation du bouton pour quitter l'application
btn_quitter = Button(root, text="X", width=4, bg='red', fg='white', command=quit)
btn_quitter.grid(row=0, column=2, sticky="e")


root.mainloop()