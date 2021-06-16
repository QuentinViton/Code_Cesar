from tkinter.messagebox import *
from tkinter import filedialog

#Fonction appelée lors du clic sur le bouton exporter
def btn_exporter_click(txt_output):
    #Affichage du menu pour choisir le chemin du fichier
    types= [( "Fichier texte" , ".txt" ), ( "Autres types" , ".*" ) ]
    file_path = filedialog.asksaveasfilename(filetypes=types , defaultextension = ".txt" )
    
    #Si un chemin a été renseigné
    if file_path:

        #Creation du fichier et ecriture du resultat dedans
        f = open(file_path, "w")
        f.write(txt_output.get(1.0, "end"))
        f.close()
    
    

#Fonction appelée lors du clic sur le bouton importer
def btn_importer_click(txt_input):
    #Affichage du menu pour choisir le chemin du fichier
    file_path = filedialog.askopenfilename()
    
    #Si un chemin a été renseigné
    if file_path:
        try:
            #Ouverture et lecture du contenu du fichier dans la zone d'input
            f = open(file_path, "r")
            txt_input.delete(1.0, "end")
            txt_input.insert(1.0, f.read())

        except Exception as e:
            #Affichage de l'erreur dans une popup si on ne peut pas ouvrir le fichier
            showerror('Erreur:', str(e))
   
    return


#Fonction appelée lors du clic sur le bouton coder
def btn_coder_click(txt_input, txt_ouput, var_decalage):
    #Si la valeur de décalage est correcte
    if var_decalage.get().isnumeric():
        #Conversion en nombre
        decalage= int(var_decalage.get())
        
        #Reset de l'output
        txt_ouput.configure(state='normal')
        txt_ouput.delete(1.0, "end")

        #Codage et affichage dans le cadre d'output
        texte_encode = Coder_cesar(txt_input.get(1.0, "end"), decalage)
        txt_ouput.insert(1.0, texte_encode)

        #Blocage de l'output en écriture
        txt_ouput.configure(state='disabled')
    else:
        #Sinon afficher que la valeur de décalage est incorrecte
        showerror('Erreur:', "Le décalage entré n'est pas un chiffre entier positif")

#Fonction appelée lors du clic sur le bouton décoder
def btn_decoder_click(txt_input, txt_ouput, var_decalage):
    #Si la valeur de décalage est correcte
    if var_decalage.get().isnumeric():
        #Conversion en nombre
        decalage= int(var_decalage.get())

        #Reset de l'output
        txt_ouput.configure(state='normal')
        txt_ouput.delete(1.0, "end")

        #Décodage et affichage dans le cadre d'output
        texte_encode = Coder_cesar(txt_input.get(1.0, "end"), -decalage)
        txt_ouput.insert(1.0, texte_encode)

        #Blocage de l'output en écriture
        txt_ouput.configure(state='disabled')
    else:
        #Sinon afficher que la valeur de décalage est incorrecte
        showerror('Erreur:', "Le décalage entré n'est pas un chifrre entier positif")

#Fonction qui décale un caractere 'c' de 'decalage' lettres dans l'alphabet et le renvoie
def Decaler_caractere(c, decalage):
    #Determination de la casse à utiliser
    if c.isupper():
        premiere_lettre='A'
    else:
        premiere_lettre='a'

    #Détermination de l'index de 'c' dans l'alphabet
    index_alphabet=ord(c)-ord(premiere_lettre)

    #Décalage de l'index dans l'alphabet
    index_alphabet += decalage

    #Modulo pour rendre l'alphabet circulaire
    index_alphabet = index_alphabet % 26

    #Retour de la lettre correspondant au nouvel index
    return chr( index_alphabet + ord(premiere_lettre))


#Fonction qui code 'texte' en Cesar en le decalant de 'decalage' lettres
def Coder_cesar(texte, decalage):
    resultat=""
    
    #Pour chacune des lettres du texte
    for caractere in texte:
        #Si le caractere est une lettre (isalpha) non accentuée (code ascii <128)
        if caractere.isalpha() and ord(caractere)<128:
            #Ajout du caractere codé
            resultat += Decaler_caractere(caractere, decalage)
        else:
            #Ajout du caractere sans codage
            resultat += caractere
    return resultat
