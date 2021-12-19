# -*- coding: utf-8 -*-
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv

def doublon(new_etudiant):
    """
    Vérifie si l'étudiant n'existe pas deja

    @param new_etudiant:
    @return:
    """
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)
    new_etudiant.pop(0)
    for etudiant in data:
        etudiant.pop(0)
        if new_etudiant == etudiant:
            return True  # Si l'étudiant existe déja

    return False


def ajoutEtudiant(*donneesEtudiant) :
    """

    @param donneesEtudiant: Liste des caractéristiques du nouvel étudiant
    @return: True si l'étudiant à bien été ajouté
    """
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)
    nouvelle_etudiant = []
    new_id = int(data[-1][0]) + 1  # Définition de l'index
    nouvelle_etudiant.append(new_id)
    for i in donneesEtudiant:
        nouvelle_etudiant.append(i)

    if doublon(nouvelle_etudiant.copy()):
        return False  # On quitte la fonction pour ne pas écrire dans le CSV

    data.append(nouvelle_etudiant)
    ecriture_fichier_csv(data, nomfichier)
    return True


def modificationEtudiant(*donneesEtudiant):
    """

    @param donneesEtudiant: Liste des caractéristiques modifié
    @return: True si la modification a été effectué
    """
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)

    modif_etudiant = []
    for i in donneesEtudiant:
        modif_etudiant.append(i)

    if doublon(modif_etudiant.copy()):
        return False

    k = 0
    for e in data:
        if e[0] == modif_etudiant[0]:
            data[k] = modif_etudiant  # On remplace avec les nouvelles données
            break
        k+=1

    ecriture_fichier_csv(data, nomfichier)
    return True


def supprimerNoteEtudiant(etudiant):
    """
    Supprime toutes les notes associé à l'ID de l'étudiant

    @param etudiant: ID de l'étudiant
    """
    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)

    i = 0
    for note in data:
        if note[2] == etudiant:
            del data[i]
        i += 1
    # Réecriture de l'index après supression de la note
    k=-1
    for note in data:
        note[0] = str(k)
        k += 1
    data[0][0] = "ID"

    ecriture_fichier_csv(data, nomfichier)


def suppressionEtudiant(etudiant) :
    """
    @param etudiant: ID de l'étudiant
    @return:
    """
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)

    k=0
    for e in data:
        if e[0] == etudiant:
            del data[k]
            break
        k += 1
    i = 0
    supprimerNoteEtudiant(etudiant)

    ecriture_fichier_csv(data, nomfichier)
    return
