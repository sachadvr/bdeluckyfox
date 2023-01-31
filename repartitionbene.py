#%%
import random
import os
import openpyxl

with open("../config/prenoms_benevoles.txt", "r") as f:
    prenoms = [prenom.strip() for prenom in f.readlines()]



# On mélange la liste de prénoms de manière aléatoire
random.shuffle(prenoms)

# on demande le nombre de personnes qui doivent être affectées
nb_affectes = int(input("Combien de personnes doivent être affectées ? "))
if nb_affectes != 0:
  prenoms = prenoms[:nb_affectes]

# On récupère la moitié de la liste
moitie_prenoms = prenoms[:len(prenoms)//2]

# On affecte les horaires 22h à 24h à la première moitié de la liste
# for prenom in moitie_prenoms:
#   print(f"{prenom} : 20h à 22h")

# # On affecte les horaires 20h à 22h à la seconde moitié de la liste
# for prenom in prenoms[len(prenoms)//2:]:
#   print(f"{prenom} : 22h à 24h")


# On crée un fichier Excel
wb = openpyxl.Workbook()

# On récupère la feuille active

ws = wb.active

# On ajoute les en-têtes

ws.append(["Prénom", "Horaires"])

# On ajoute les prénoms et les horaires

for prenom in prenoms:
    if prenom in moitie_prenoms:
        ws.append([prenom, "20h à 22h"])
    else:
        ws.append([prenom, "22h à 24h"])

# On sauvegarde le fichier Excel

wb.save("horaires.xlsx")

# On ferme le fichier Excel

wb.close()

# On affiche un message de confirmation

print("Fichier Excel créé avec succès")
# ouvre le fichier excel
os.startfile("horaires.xlsx")

