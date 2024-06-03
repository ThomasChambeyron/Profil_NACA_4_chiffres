# Le script suivant permet de générer un profil d'aile NACA 4 chiffres symétrique.
# L'utilisateur renseignele numéro du profil, la longueur de la corde, le nombre de points permettant de tracer ce profil,
# ainsi que le type de distribution (uniforme ou non-uniforme). Le programme trace ensuite le profil de l'aile et indique
# à l'utilisateur l'épaisseur maximale du profil et sa position le long de la corde.
# Le script est décomposé en 4 fonctions. L'idée est de créer l'intervalle de points dans un premier temps (generer_xc()),
# pour ensuite calculer les coordonnées de chaque points (calculer_coordonnees()) et les tracer sur un graphe (tracer_profil()).
# Une fonction a également été définie pour calculer l'épaisseur maximale du profil (calculer_epaisseur_max()).

# Import de la librairie numpy et matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Fonction qui génère les coordonnées xc en fonction du nombre de points et du type de distribution choisi
def generer_xc(nb_points, type_distribution):
    if type_distribution == 'uniforme':
        return np.linspace(0, 1, nb_points) # Génération d'un interval de points uniformément répartis
    elif type_distribution == 'non-uniforme':
        theta = np.linspace(0, np.pi, nb_points) # Génération d'un interval de points non-uniformément répartis
        return 0.5 * (1 - np.cos(theta))
    else:
        raise ValueError("Type de distribution invalide. Choisissez 'uniforme' ou 'non-uniforme'.")

# Fonction qui calcule les coordonnées des points sur les courbes de l'extrados et de l'intrados en fonction de xc, de la corde c et de l'épaisseur maximale t.
def calculer_coordonnees(xc, c, t):
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    xup = xc * c
    yup = yt * c
    xdown = xc * c
    ydown = -yt * c
    return xup, yup, xdown, ydown

# Calcule l'épaisseur maximale et sa position le long de la corde.
def calculer_epaisseur_max(yt):
    epaisseur_max = np.max(yt) * 100  # Détermination de l'épaisseur maximale ytmax grace a la fonction np.max(), conversion en %
    position_max = (np.argmax(yt) / len(yt)) * 100  # Position de l'épaisseur maximale en % de la corde via la fonction argmax() qui renvoie l'argument de ytmax
    return epaisseur_max, position_max

# Fonction qui permet de tracer le profil de l'aile et d'afficher les légendes appropriées.
def tracer_profil(xup, yup, xdown, ydown, numero_profil):
    plt.figure(figsize=(10, 5))
    plt.plot(xup, yup, label='Extrados')
    plt.plot(xdown, ydown, label='Intrados')
    plt.title(f'Profil NACA {numero_profil}')
    plt.xlabel('x (mètres)')
    plt.ylabel('y (mètres)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


# Récupérer les entrées de l'utilisateur
numero_profil = input("Entrez le numéro du profil NACA 4 chiffres symétrique (ex. : 0012) : ")
c = float(input("Entrez la longueur de la corde en mètres : "))
nb_points = int(input("Entrez le nombre de points le long de la corde : "))
type_distribution = input("Entrez le type de distribution (uniforme ou non-uniforme) : ")

# Extraire le pourcentage d'épaisseur à partir du numéro du profil
t = int(numero_profil[-2:]) / 100

# Générer xc en fonction du choix de l'utilisateur
xc = generer_xc(nb_points, type_distribution)

# Calculer les coordonnées
xup, yup, xdown, ydown = calculer_coordonnees(xc, c, t)

# Calculer l'épaisseur maximale et sa position
epaisseur_max, position_max = calculer_epaisseur_max(yup)

# Afficher les résultats
print(f"Épaisseur maximale : {epaisseur_max:.1f} %")
print(f"Position de l'épaisseur maximale le long de la corde : {position_max:.1f} %")

# Tracer le profil
tracer_profil(xup, yup, xdown, ydown, numero_profil)
