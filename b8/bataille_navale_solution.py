#!/opt/local/bin/python
# -*- coding: utf-8 -*-
from sense_hat import SenseHat

sense = SenseHat()

# la grille de jeu virtuelle est composée de 8 x 8 cases
# (elle est constituée de 10 x 10 cases dans le jeu original)
# une case est identifiée par ses coordonnées (no_ligne, no_colonne)
# un no_ligne ou no_colonne est compris entre 1 et 8

TAILLE_GRILLE = 8
COULEUR_MER        = (0,   0,   204)
COULEUR_TIR_RATE   = (128, 128, 128)
COULEUR_TIR_TOUCHE = (255, 128, 0)
COULEUR_TIR_COULE  = (204, 0, 0)

# chaque navire est constitué d'un dictionnaire dont les clés sont les
# coordonnées de chaque case le composant, et les valeurs correspondantes
# l'état de la partie du navire correspondant à la case
# (True : intact ; False : touché) 

# les navires suivants sont disposés de façon fixe dans la grille :
#     +---+---+---+---+---+---+---+---+
#     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
# +---+---+---+---+---+---+---+---+---+
# | 1 |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+
# | 2 |   | o | o | o | o | o |   |   |
# +---+---+---+---+---+---+---+---+---+
# | 3 |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+
# | 4 | o |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+
# | 5 | o |   | o |   |   | o | o | o |
# +---+---+---+---+---+---+---+---+---+
# | 6 | o |   | o |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+
# | 7 | o |   | o |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+
# | 8 |   |   |   |   | o | o |   |   |
# +---+---+---+---+---+---+---+---+---+
porte_avion       = {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}
croiseur          = {(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True}
contre_torpilleur = {(5, 3): True, (6, 3): True, (7, 3): True}
sous_marin        = {(5, 6): True, (5, 7): True, (5, 8): True}
torpilleur        = {(8, 5): True, (8, 6): True}
liste_navires = [porte_avion, croiseur, contre_torpilleur, sous_marin, torpilleur]

# transforme des coordonnées de la grille virtuelle en
# coordonnées de l'écran LED du Sense HAT
def coord_grille_vers_coord_LED(coord):
    no_lig = coord[0]
    no_col = coord[1]
    return (no_col - 1, no_lig - 1)

# affiche le pixel correspondant aux coordonnées de la grille
# virtuelle avec la couleur passée en paramètre
def affiche_coord_couleur(coord, couleur):
    (x, y) = coord_grille_vers_coord_LED(coord)
    sense.set_pixel(x, y, couleur)

# au départ, toutes les cases sont présumées être de l'eau
def init_LED():
    for coord in \
        [(no_lig, no_col)
            for no_lig in range(1, TAILLE_GRILLE + 1)
                for no_col in range(1, TAILLE_GRILLE + 1)]:
        affiche_coord_couleur(coord, COULEUR_MER)

# demande un no de ligne ou de colonne
def demande_no_lig_col():
    try:
        no = int(input())
        no_valide = no >= 1 and no <= TAILLE_GRILLE
    except ValueError:
        no_valide = False

    if not no_valide:
        print('Entrez un entier entre 1 et {}'.format(TAILLE_GRILLE))
        no = demande_no_lig_col()
    return no

# demande les coordonnées d'une case de la grille
def demande_coord():
    print('Entrez les coordonnées de votre tir : n° de ligne de la case, puis son n° de colonne')
    no_lig = demande_no_lig_col()
    no_col = demande_no_lig_col()
    return (no_lig, no_col)

# indique si un navire est touché par un tir aux coordonnées indiquées,
# et si c'est le cas :
# - mémorise que la partie du navire correspondante est touchée
# - affiche la case correspondante comme touchée
# - si le navire est alors coulé, l'affiche en entier comme tel
def navire_est_touche(navire, coord):
    est_touche = coord in navire
    if est_touche:
        print('Un navire a été touché par votre tir !')
        navire[coord] = False
        # afficher la case correspondante comme touchée
        affiche_coord_couleur(coord, COULEUR_TIR_TOUCHE)
        if navire_est_coule(navire):
            print('Le navire touché est coulé !!')
            couler_navire(navire)

    return est_touche

# indique si un navire touché par un tir est coulé
def navire_est_coule(navire):
    return not any(navire.values())

# affiche toutes les cases d'un navire coulé avec la couleur correspondante
def couler_navire(navire):
    for coord in navire:
        (no_lig, no_col) = coord
        # afficher la case correspondante comme coulée
        affiche_coord_couleur(coord, COULEUR_TIR_COULE)
    # le navire est supprimé de la flotte
    liste_navires.remove(navire)

# -------------------------------------------------------------------------- #
# programme principal :                                                      #
# tant que tous les navires ne sont pas coulés, on demande au joueur         #
# d'indique une case où il souhaite effectuer un tir                         #
# -------------------------------------------------------------------------- #
init_LED()
while liste_navires:
    coord = demande_coord()
    if not any([navire_est_touche(navire, coord) for navire in liste_navires]):
        print("Votre tir est tombé dans l'eau")
        # afficher la case correspondante comme un tir raté
        affiche_coord_couleur(coord, COULEUR_TIR_RATE)
print('Bravo, vous avez coulé tous les navires')