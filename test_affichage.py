from time import time

d = time()

from carac import *
from classes import Analyseur, Probleme
from Clustering.kmeans import Kmeans
from Clustering.kmedoids import KMedoids

d = time()

oeuvres_training_set =[("zola",k) for k in range(1,3)] + [("balzac",k) for k in range(1,3)] + [("maupassant",k) for k in range(1,3)]
oeuvres_eval_set = [("zola",k) for k in range(3,5)] + [("balzac",k) for k in range(3,5)]
taille_morceaux = 3000


analyseur = Analyseur([freq_stopwords])
classifieur = KMedoids()

P = Probleme(oeuvres_training_set, oeuvres_eval_set, taille_morceaux, analyseur, classifieur, langue = "fr")

#P.resoudre() equivalent a

P.creer_textes(equilibrage = False)
P.analyser(normalisation = True)
P.appliquer_classifieur()
P.afficher_graphique()

f = time()
print()
print("Temps d'exécution : " + str(f-d) + "s")

P.afficher()