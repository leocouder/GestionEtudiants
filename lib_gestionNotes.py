# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def ajoutNote(*donneesNote) :
    """
    Ajoute une nouvelle note au CSV

    @param donneesNote:
    @return:
    """
    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)
    nouvelle_note = []
    nouvelle_note.append(len(data)-1)  # Définition de l'index
    for i in donneesNote:
        nouvelle_note.append(i)
    data.append(nouvelle_note)
    ecriture_fichier_csv(data, nomfichier)
    return

def modificationNote(*donneesNote) :
    """
    Modification d'une note existante

    @param donneesNote:
    @return:
    """
    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)

    supp_note = []
    for i in donneesNote:
        supp_note.append(i)
    for note in data:
        if note[1] == supp_note[0] and note[2] == supp_note[1] and note[3] == supp_note[2]:
            note[4] = supp_note[3]  # On peux modifier uniquement la note
    ecriture_fichier_csv(data, nomfichier)
    return

def suppressionNote(*donneesNote) :
    """
    Suppression d'une note

    @rtype: object
    """
    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)
    supp_note = []
    for i in donneesNote:
        supp_note.append(i)

    i = 0
    for note in data:
        if supp_note[0] == note[1] and supp_note[1] == note[2] and supp_note[2] == note[3] and supp_note[3] == note[4]:
            del data[i]
        i+=1

    #Réecriture de l'index après supression de la note
    k=-1
    for note in data:
        note[0] = str(k)
        k += 1
    data[0][0] = "ID"

    ecriture_fichier_csv(data, nomfichier)
    return
