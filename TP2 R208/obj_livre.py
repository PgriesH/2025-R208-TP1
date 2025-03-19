from obj_couleur import Couleur
from obj_auteurs import Auteur


class Livre(Couleur):
    nombre_total_livres = 0

    def __init__(self, titre, auteur, isbn=None, annee_publication=None, disponible=True):
        Livre.incr_nb_livres()
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur
        if isbn is None:
            self.isbn = "N/A"
        else:
            self.isbn = isbn
        if annee_publication is None:
            self.annee_publication = "inconnue"
        else:
            self.annee_publication = annee_publication
        self.disponible = disponible

    def __str__(self):
        str1 = f'{Livre.BLEU}{self.id}\t: {Livre.NO_COLOR}{self.titre} de {self.auteur.prenom} {self.auteur.nom}{Livre.MAGENTA} ISBN: {self.isbn} publié en {self.annee_publication}'
        str2 = f'{Livre.VERT} Dispo' if self.disponible else f'{Livre.ROUGE} NON Dispo'
        return str1 + str2

    @classmethod
    def incr_nb_livres(cls):
        Livre.nombre_total_livres += 1
