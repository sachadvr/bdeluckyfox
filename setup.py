#%%
# 
print ("Bonjour, bienvenue dans le programme de repartition des horaires de la soirée du BDE !")
print("--------------------------------------------")
print("1. Repartition de tout le monde")
print("2. Repartition des benevoles")
choix = int(input("Que voulez-vous faire ? "))
if choix == 1:
    import repartition
elif choix == 2:
    import repartitionbene
else:
    print("Choix invalide")

