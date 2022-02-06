# -*- coding: utf-8 -*-
"""
Created on Sat Dec 04 14:01:14 2021

@author: ThomasBAGHRI
"""

import pandas
import random
from random import choice
import string

#On importe le fichier csv sous le nom 'liste' avec le module pandas
liste = pandas.read_csv("liste_eleves.csv")
liste.loc[0, 'ID'] = '0'

#On crée l'ID des utilisateurs
for ligne in range (len(liste)):
    #var: prnm = prénom, nm = nom, usrnm = ID
    prnm = liste.loc[ligne, 'prenom'][0] #On ne récupère que la première lettre du prénom
    prnm = prnm.lower()
    nm = liste.loc[ligne, 'nom']
    nm = nm.lower()
    #On forme l'ID à partir du prénom et du nom
    usrnm = prnm + nm
    
    #Créer l'identifiant unique
    usrnmcnt  = 1 #numéro ajouté à la fin des ID doublons
    usrnmFinal = usrnm #ID définitif assigné
    usrnmFinalTrouve = False #variable permettant de savoir si le calcul de l'ID est terminé
    
    while (usrnmFinalTrouve == False): #On cherche si l'ID est unique
        trouve = False
        l = 0
        while(trouve == False and l < ligne ): #tant que l'ID est unique et que 
        #la ligne de recherche est inférieure à la ligne on continue
            if(liste.loc[l, 'ID'] == usrnmFinal):
                trouve = True
            l=l+1

        if(trouve == True): #si on trouve un ID identique, on rajoute +1 au
        #compteur jusqu'à ce que l'ID soit unique
            usrnmFinal = usrnm + str(usrnmcnt)
            print(usrnmFinal)
            usrnmcnt = usrnmcnt + 1
        else:
            usrnmFinalTrouve = True
        
    #On enregistre l'ID dans une nouvelle colonne "ID"
    liste.loc[ligne, 'ID'] = usrnmFinal



#On assigne le mot de passe
for ligne in range(len(liste)):
    #var: mdp = mot de passe, carac = caractères définis aléatoirement
    mdp = ""
    carac = string.ascii_lowercase + string.digits
    #On utilise et réitère 8 fois la fonction choice du module random pour choisir les 8 caractères
    for i in range (8):
        mdp = mdp + (choice(carac))
        
    #On enregistre le mdp dans une nouvelle colonne "MdP"
    liste.loc[ligne,'MdP'] = mdp
    
print(liste)

#On enregistre la DataFrame 'liste' importée en haut du programme en tant que
#liste_complétée.csv
liste.to_csv("liste_complete.csv")