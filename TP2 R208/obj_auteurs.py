from obj_couleur import Couleur


class Auteur(Couleur):
    nombre_total_auteur = 0

    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.incr_nb_auteurs()
        self.id = Auteur.nombre_total_auteur
        self.nom = nom
        self.prenom = prenom
        if pays is None:
            self.pays = "Inconnu"
        else:
            self.pays = pays
        if date_naissance is None:
            self.date_naissance = "Inconnue"
        else:
            self.date_naissance = date_naissance

    def __str__(self):
        return f'{Auteur.BLEU}{self.id},\t:{Auteur.NO_COLOR}{self.prenom}{self.nom}{Auteur.MAGENTA}(né(e) le {self.date_naissance} en {self.pays})'

    @classmethod
    def incr_nb_auteurs(cls):
        Auteur.nombre_total_auteur += 1
