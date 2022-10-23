from random import*

def debutant(mot, mot_devine):
    vie = 10
    lettreUtilise= ""
    while mot_devine!=mot and vie != 0 :
        reussi = False
        print("Nombre de vie(s) restante(s) : ", vie)
        print("Lettre proposé :", lettreUtilise)
        print(mot_devine)
        lettre = str(input("Quelle lettre proposes tu ? "))
        for i in range(len(mot)):
            if lettre==mot[i]:
                mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
                reussi = True
                bonneLettre = True
        if(reussi == True):
            vie += 1

        lettreUtilise += lettre + " "

        vie -= 1
            
    if mot == mot_devine:
        print ('Bravo ! Le mot',mot,'a été trouvé')
    else:
        print("Dommage c'est perdu le mot était",mot)

def intermediaire(mot, mot_devine):
    vie = 7
    lettreUtilise= ""
    while mot_devine!=mot and vie != 0 :
        reussi = False
        print("Nombre de vie(s) restante(s) : ", vie)
        print("Lettre proposé :", lettreUtilise)
        print(mot_devine)
        lettre = str(input("Quelle lettre proposes tu ? "))
        for i in range(len(mot)):
            if lettre==mot[i]:
                mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
                reussi = True
                bonneLettre = True
        if(reussi == True):
            vie += 1

        lettreUtilise += lettre + " "

        vie -= 1
            
    if mot == mot_devine:
        print ('Bravo ! Le mot',mot,'a été trouvé')
    else:
        print("Dommage c'est perdu le mot était",mot)

def expert(mot, mot_devine):
    vie = 4
    while mot_devine!=mot and vie != 0 :
        reussi = False
        print("Nombre de vie(s) restante(s) : ", vie)
        print(mot_devine)
        lettre = str(input("Quelle lettre proposes tu ? "))
        for i in range(len(mot)):
            if lettre==mot[i]:
                mot_devine = mot_devine[:i] + lettre + mot_devine[i+1:]
                reussi = True
        if(reussi == True):
            vie += 1
        vie -= 1
            
    if mot == mot_devine:
        print ('Bravo ! Le mot',mot,'a été trouvé')
    else:
        print("Dommage c'est perdu le mot était",mot)

fichier = open("dico_france.txt", "r")
liste_mots = fichier.readlines()    
mot = choice(liste_mots)            
mot = mot.rstrip()                 
fichier.close()

mot_devine = "_" * len(mot)

difficulte = str(input("Bonjour, à quel niveau souhaites tu jouer ? "))

match difficulte:
    case "Débutant":
        debutant(mot, mot_devine)
    case "Intermédiaire":
        intermediaire(mot, mot_devine)
    case "Expert":
        expert(mot, mot_devine)
