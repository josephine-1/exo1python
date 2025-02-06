#Convention de Nommage
print ("Hello Wordl!c'est mon premier projet python")
nom = "DIOP"
print (nom)
#Déclaration Variable
age_2019 = 20
age_2020 = age_2019 + 1
print("2019",age_2019)
print("2020",age_2020)
age_reel = 32.5
age_entier = int(age_reel)
print (age_entier)
#Les listes/array
ma_list = ["Astou" ,"Fatou","Aicha" ,2,25]
#Afficher la liste
print (ma_list)
#Afficher le premier Elément
print (ma_list[0])
#Afficher le nombre d'élément
print(len(ma_list))
#Tuple comme liste mais on ne peut pas modifier les éléments
mon_tuple = ("Login","Mot de passe")

#Dictionnaire clé-valeur
mon_dict = {
    "nom":"DIOP" ,
    "prenom" :"Joséphine",
    "Adresse" :"Thiaroye"
}
print (mon_dict)
#Pour recupéré une clé dans une liste on appel la méthode get
print (mon_dict.get("Adresse"))