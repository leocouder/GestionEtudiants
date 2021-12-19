import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lib_commun import ouverture_fichier_csv
from lib_gestionEtudiants import ajoutEtudiant, modificationEtudiant, suppressionEtudiant
from lib_gestionNotes import ajoutNote, modificationNote, suppressionNote


def selectItemNote(a):
    """
    Récupère les valeurs de la ligne selectionné dans le treeview
    @param a:
    """
    curItem = tree_note.focus()
    curItem_data = tree_note.item(curItem)
    annee.set(curItem_data['values'][1])
    id_e.set(curItem_data['values'][2])
    matiere.set(curItem_data['values'][3])
    note.set(curItem_data['values'][4])


def selectItemEtudiant(a):
    """
    Affiche les valeurs de la ligne sélectionné dans le Treeview
    @param a:
    """
    curItem = tree_etudiant.focus()
    curItem_data = tree_etudiant.item(curItem)
    prenom.set(curItem_data['values'][3])
    nom.set(curItem_data['values'][2])
    email.set(curItem_data['values'][4])
    id_value.set(curItem_data['values'][0])
    if curItem_data['values'][1] == "M":
        Male.select()
    else:
        Female.select()


def get_data_note():
    """
    Récupère les valeurs entrées par l'utilisateur
    @return: Liste des données
    """
    annee_note = annee.get()
    id_etudiant = id_e.get()
    matiere_note = matiere.get()
    note_etudiant = note.get()

    data = [annee_note, id_etudiant, matiere_note, note_etudiant]
    input_id_e.delete(0, tkinter.END)
    input_note.delete(0, tkinter.END)
    input_matiere.delete(0, tkinter.END)
    input_annee.delete(0, tkinter.END)

    return data


def get_data_etudiant():
    """
    Récupère les valeurs entrées par l'utilisateur
    @return: Liste des données
    """
    prenom_etudiant = prenom.get()
    nom_etudiant = nom.get()
    sex_etudiant = sex.get()
    email_etudiant = email.get()
    id_etudiant = id_value.get()
    data = [sex_etudiant, nom_etudiant, prenom_etudiant, email_etudiant, id_etudiant]

    input_prenom.delete(0, tkinter.END)
    input_nom.delete(0, tkinter.END)
    input_email.delete(0, tkinter.END)
    id_value.set("")

    return data

"""
    Toutes les fonctions qui suivents sont appellé lors de l'appui
    sur l'un des boutons de l'interface Tkinter.
    
    Elles permettent l'ajout, la modification et la suppression des étudiants ou leurs notes.
"""

def ajouter_etudiant():
    data = get_data_etudiant()
    for i in range(4):
        if data[i] == "":
            # message d'erreur
            messagebox.showwarning("Erreur", "Vous n'avez pas rempli tous les champs")
            return

    if not ajoutEtudiant(data[0], data[1], data[2], data[3]):
        messagebox.showwarning("Erreur", "L'étudiant existe déja")
    refresh_treeview_etudiant()


def ajouter_note():
    data = get_data_note()
    for champs in data:
        if champs == "":
            messagebox.showwarning("Erreur", "Vous n'avez pas rempli tous les champs")
            return
    ajoutNote(data[0], data[1], data[2], data[3])
    refresh_treeview_note()


def modifier_etudiant():
    data = get_data_etudiant()
    for champs in data:
        if champs == "":
            messagebox.showwarning("Erreur", "Vous n'avez pas rempli tous les champs")
            return
    if not modificationEtudiant(data[4], data[0], data[1], data[2], data[3]):
        messagebox.showwarning("Erreur", "L'étudiant existe déja")
    refresh_treeview_etudiant()


def modifier_note():
    data = get_data_note()
    for champs in data:
        if champs == "":
            messagebox.showwarning("Erreur", "Vous n'avez pas rempli tous les champs")
            return
    modificationNote(data[0], data[1], data[2], data[3])
    refresh_treeview_note()


def supp_etudiant():
    id_etudiant = id_value.get()
    id_value.set("")

    suppressionEtudiant(id_etudiant)
    refresh_treeview_etudiant()
    refresh_treeview_note()
    messagebox.showinfo("Suppression", "L'étudiant ainsi que toutes ces notes ont été supprimées")


def supp_note():
    data = get_data_note()
    suppressionNote(data[0], data[1], data[2], data[3])
    refresh_treeview_note()


def refresh_treeview_etudiant():
    """
    Met à jour le treeview étudiant
    """
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)
    for i in tree_etudiant.get_children():
        tree_etudiant.delete(i)
    del data[0]
    for etudiant in data:
        # Ajout de chaque ligne
        tree_etudiant.insert('',tkinter.END, values=etudiant)


def refresh_treeview_note():
    """
    Met à jour le treeview note
    """
    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)
    for i in tree_note.get_children():
        tree_note.delete(i)
    del data[0]
    for etudiant in data:
        tree_note.insert('',tkinter.END, values=etudiant)


def vider_input():
    """
    Efface les caractères écrits dans les champs
    """
    input_prenom.delete(0, tkinter.END)
    input_nom.delete(0, tkinter.END)
    input_email.delete(0, tkinter.END)
    id_value.set("")
    input_id_e.delete(0, tkinter.END)
    input_note.delete(0, tkinter.END)
    input_matiere.delete(0, tkinter.END)
    input_annee.delete(0, tkinter.END)


fenetre = Tk()
fenetre.title("Gestion Scolaire")
fenetre.geometry('900x600')
fenetre.resizable(height=False, width=False)  # Bloque le redimensionnement de la page

onglet = ttk.Notebook(fenetre)
onglet.grid(column=1, row=1)
onglet2 = ttk.Frame(onglet)
onglet3 = ttk.Frame(onglet)
onglet.add(onglet2, text="Etudiants")
onglet.add(onglet3, text="Notes")

# ----------- Premier onglet ------------

formulaire_etudiant = Frame(onglet2, relief=GROOVE)
formulaire_etudiant.pack(padx=(80,10), pady=10)

Title = Label(formulaire_etudiant, text="Etudiants", font=25)
Title.grid(column=1, columnspan=4, row=1)

# Variable que l'on pourra récupérer
sex = StringVar()
prenom = StringVar()
nom = StringVar()
email = StringVar()

label_prenom = Label(formulaire_etudiant, text="Prénom")
label_prenom.grid(pady=(15,0),column=1, row=2)
input_prenom = Entry(formulaire_etudiant, width=30, textvariable=prenom)
input_prenom.grid(pady=(15,0),column=2, columnspan=2, row=2)

label_nom = Label(formulaire_etudiant, text="Nom")
label_nom.grid(pady=(15,0),column=1, row=4)
input_nom = Entry(formulaire_etudiant, textvariable=nom, width=30)
input_nom.grid(pady=(15,0),column=2, columnspan=2, row=4)


sex_label = Label(formulaire_etudiant, text="Sexe")
sex_label.grid(pady=(15,0),column=1, row=6)
Female = Radiobutton(formulaire_etudiant, text="F", variable=sex, value="F")
Female.grid(pady=(15,0),column=2,row=6)
Male = Radiobutton(formulaire_etudiant, text="M", variable=sex, value="M")
Male.grid(pady=(15,0),column=3, row=6)
sex.set("M")

email_label = Label(formulaire_etudiant, text="Email")
email_label.grid(pady=(15,0),column=1, row=8)
input_email = Entry(formulaire_etudiant, textvariable=email, width=30)
input_email.grid(pady=(15,0),column=2, columnspan=2, row=8)

ajouter = Button(formulaire_etudiant, text = "Ajouter", bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2, command=ajouter_etudiant)
ajouter.grid(padx=10,pady=(15,15),column=1, row=10)
modifier = Button(formulaire_etudiant, text = "Modifier",bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2, command=modifier_etudiant)
modifier.grid(padx=10,pady=(15,15),column=2, row=10)
supprimer = Button(formulaire_etudiant, text = "Supprimer",bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2, command=supp_etudiant)
supprimer.grid(padx=10,pady=(15,15),column=3, row=10)
bouton_vider = Button(formulaire_etudiant, text = "Vider",bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2, command=vider_input)
bouton_vider.grid(padx=10,pady=(15,15),column=4, row=10)

id_value = StringVar()
label_id = Label(formulaire_etudiant, text="ID")
label_id.grid(pady=(15,0),column=2, row=9)
label_id_value = Label(formulaire_etudiant, textvariable=id_value)
label_id_value.grid(pady=(15,0),column=3, row=9)

frame_etudiant = Frame(onglet2, relief=GROOVE)
frame_etudiant.pack(padx=(80,0), pady=10)

colonne=('ID','SEX','NOM','PRENOM','EMAIL')
tree_etudiant = ttk.Treeview(frame_etudiant, columns=colonne, show="headings")
# Dimensions des colonnes
tree_etudiant.column("ID",minwidth=0,width=50)
tree_etudiant.column("SEX",minwidth=0,width=50)
tree_etudiant.column("NOM",minwidth=0,width=150)
tree_etudiant.column("PRENOM",minwidth=0,width=150)
tree_etudiant.column("EMAIL",minwidth=0,width=300)
tree_etudiant.heading('ID', text="ID")
tree_etudiant.heading('SEX', text="SEX")
tree_etudiant.heading('NOM', text="NOM")
tree_etudiant.heading('PRENOM', text="PRENOM")
tree_etudiant.heading('EMAIL', text="EMAIL")
refresh_treeview_etudiant()
tree_etudiant.pack(padx=(0,50))

tree_etudiant.bind("<<TreeviewSelect>>", selectItemEtudiant)


# ---------- Deuxieme onglet ----------------


formulaire_note = Frame(onglet3, relief=GROOVE)
formulaire_note.pack(padx=(80,10), pady=10)

Titre = Label(formulaire_note, text="Notes", font=25)
Titre.grid(column=1,columnspan=4, row=0)

annee = StringVar()
id_e = StringVar()
matiere = StringVar()
note = StringVar()

label_annee = Label(formulaire_note, text="Année")
label_annee.grid(pady=(15,0),column=1, row=1)
input_annee = Entry(formulaire_note, width=30, textvariable=annee)
input_annee.grid(pady=(15,0),column=2, columnspan=3, row=1)

label_id_e = Label(formulaire_note, text="Id étudiant")
label_id_e.grid(pady=(15,0),column=1, row=2)
input_id_e = Entry(formulaire_note, textvariable=id_e, width=30)
input_id_e.grid(pady=(15,0),column=2, columnspan=3, row=2)

label_matiere = Label(formulaire_note, text="Matière")
label_matiere.grid(pady=(15,0), column=1, row=3)
data_matiere = ouverture_fichier_csv("matieres.csv")
input_matiere = ttk.Combobox(formulaire_note, values=data_matiere, width=27, textvariable=matiere)
input_matiere.grid(pady=(15,0), column=2, columnspan=3, row=3)
"""input_matiere = Entry(formulaire_note, textvariable=matiere, width=30)
input_matiere.grid(pady=(15,0), column=2, columnspan=3, row=3)"""

label_note = Label(formulaire_note, text="Note")
label_note.grid(pady=(15,0),column=1, row=4)
input_note = Entry(formulaire_note, textvariable=note, width=30)
input_note.grid(pady=(15,0),column=2, columnspan=3, row=4)

ajouter_note = Button(formulaire_note, text = "Ajouter", command=ajouter_note, bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2)
ajouter_note.grid(padx=10,pady=(30,0),column=1, row=5)
modif_note = Button(formulaire_note, text = "Modifier", command=modifier_note, bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2)
modif_note.grid(padx=10,pady=(30,0),column=2,row=5)
supp_note = Button(formulaire_note, text = "Supprimer", command=supp_note, bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2)
supp_note.grid(padx=10,pady=(30,0),column=3, row=5)
bouton_vider = Button(formulaire_note, text = "Vider", command=vider_input, bg="#98D2EB", activebackground="#B2B1CF", width=10, height=2)
bouton_vider.grid(padx=10,pady=(30,0),column=4, row=5)

attention = Label(formulaire_note, text="Attention ! Seule la note peut etre modifié")
attention.grid(column=1,columnspan=4, row=6)

frame_note = Frame(onglet3, relief=GROOVE)
frame_note.pack(padx=(80,0), pady=10)

colonne=('ID','ANNEE SCOLAIRE','ID_ETUDIANT','MATIERE','NOTE')
tree_note = ttk.Treeview(frame_note, columns=colonne, show="headings")
tree_note.column("ID",minwidth=0,width=50)
tree_note.column("ANNEE SCOLAIRE",minwidth=0,width=100)
tree_note.column("ID_ETUDIANT",minwidth=0,width=150)
tree_note.column("MATIERE",minwidth=0,width=150)
tree_note.column("NOTE",minwidth=0,width=300)
tree_note.heading('ID', text="ID")
tree_note.heading('ANNEE SCOLAIRE', text="ANNEE SCOLAIRE")
tree_note.heading('ID_ETUDIANT', text="ID_ETUDIANT")
tree_note.heading('MATIERE', text="MATIERE")
tree_note.heading('NOTE', text="NOTE")
refresh_treeview_note()
tree_note.pack(padx=(0,50))
tree_note.bind("<<TreeviewSelect>>", selectItemNote)

fenetre.mainloop()