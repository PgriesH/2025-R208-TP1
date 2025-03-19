from obj_couleur import Couleur


class Membre(Couleur):
    nombre_total_membres = 0

    def __init__(self, nom, prenom, date_naissance):
        Membre.incr_nb_membres()
        self.id = Membre.nombre_total_membres
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.livres_empruntes = []

    def __str__(self):
        return f'{Membre.BLEU}{self.id}\t: {Membre.NO_COLOR}{self.prenom} {self.nom}{Membre.MAGENTA} né(e) le {self.date_naissance}{Membre.NO_COLOR}'

    def lister_emprunts(self):
        if self.livres_empruntes == []:
            print(f'\t{Membre.ROUGE}///{Membre.NO_COLOR}\t {self.prenom} {self.nom} n\'a aucun livre empruntés')
        else:
            print(f'\t{Membre.ROUGE}->{Membre.VERT}\t {self.prenom} {self.nom} a emprunté les livres suivants')
            for liv in self.livres_empruntes:
                print(liv)

    def emprunter_livre(self, livre):
        if livre.disponible == True:
            self.livres_empruntes.append(livre)
            livre.disponible = False
            print(f'\t --> {self.prenom} {self.nom} a emprunté {livre.titre}')
        else:
            print(f'Le livre {livre.titre} n\'est plus disponible a l\'emprunt')

    def restituer_livre(self, livre):
        if livre.disponible == True:
            print(f'Le livre {livre.titre} n\'est pas emprunté en ce moment')
        else:
            for liv in self.livres_empruntes:
                if liv.titre == livre.titre:
                    self.livres_empruntes.remove(liv)
                    liv.disponible = True
                    print(f'Le livre {livre.titre} a été restitué par {self.prenom} {self.nom}')
                else:
                    print(f'Le livre {livre.titre} n\'est pas emprunté par le membre {self.prenom} {self.nom}')

    @classmethod
    def incr_nb_membres(cls):
        Membre.nombre_total_membres += 1
