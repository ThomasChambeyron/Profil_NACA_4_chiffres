# Générateur de Profil NACA 4 Chiffres Symétrique

Ce projet génère des profils d'ailes NACA à 4 chiffres symétriques et visualise la forme du profil en fonction des paramètres fournis par l'utilisateur. Il calcule également l'épaisseur maximale et sa position le long de la corde.

## Fonctionnalités

* Génération de coordonnées pour des profils d'ailes NACA à 4 chiffres symétriques.
* Choix de la distribution uniforme ou non-uniforme (transformée de Glauert) des points le long de la corde.
* Calcul de l'épaisseur maximale et de sa position le long de la corde.
* Visualisation graphique du profil de l'aile avec indication de l'épaisseur maximale.

## Prérequis

Avant de commencer, assurez-vous d'avoir les bibliothèques Python suivantes installées :
* numpy
* matplotlib
Vous pouvez les installer en utilisant les commandes suivantes : _**pip install numpy matplotlib**_

## Utilisation

1. Téléchargez le fichier main.py.
2. Exécutez le script main.py dans votre environnement Python préféré.
3. Entrez les informations demandées lorsque vous y êtes invité :
   * Numéro du profil NACA : Entrez un numéro de profil NACA à 4 chiffres symétrique (par exemple, 0012).
   * Longueur de la corde : Entrez la longueur de la corde en mètres (par exemple, 1.0).
   * Nombre de points : Entrez le nombre de points le long de la corde pour le tracé (par exemple, 100).
   * Type de distribution : Entrez le type de distribution des points (uniforme ou non-uniforme).
Le script calculera les coordonnées du profil, l'épaisseur maximale et sa position, puis affichera un graphique du profil de l'aile.

## Exemple

Voici un exemple d'utilisation du script (Les entrées de l'utilisateur sont spécifiées en **gras**):

Entrez le numéro du profil NACA 4 chiffres symétrique (ex. : 0012) : **0012**
Entrez la longueur de la corde en mètres : **1.0**
Entrez le nombre de points le long de la corde : **100**
Entrez le type de distribution (uniforme ou non-uniforme) : **non-uniforme**

Les résultats affichés seront :

Épaisseur maximale : 12.0 % 
Position de l'épaisseur maximale le long de la corde : 30.0 % 
Et un graphique montrant le profil de l'aile avec une annotation indiquant l'extrados et l'intrados.

## Structure du Code

_generer_xc(nb_points, type_distribution)_ : Génère les coordonnées xc en fonction du nombre de points et du type de distribution choisi (uniforme ou non-uniforme).
_calculer_coordonnees(xc, c, t)_ : Calcule les coordonnées des points sur les courbes de l'extrados et de l'intrados en fonction de xc, de la corde c et de l'épaisseur maximale t.
_calculer_epaisseur_max(yt, c)_ : Calcule l'épaisseur maximale et sa position le long de la corde.
_tracer_profil(xup, yup, xdown, ydown, numero_profil)_ : Trace le profil de l'aile avec les annotations et les légendes appropriées.
