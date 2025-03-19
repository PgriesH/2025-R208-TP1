from obj_auteurs import Auteur
from obj_livre import Livre
from obj_membre import Membre

if __name__ == "__main__":
    print("Création de 3 instances de Auteur et affichage...")
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)
    print(follett)
    print(verne)
    print(bridou)
    print(bridou.pays)
    print(bridou.date_naissance)

    print("Création de 3 instances de Livre et affichage...")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
    livre_2.disponible = False
    livre_3 = Livre("Vingt Mille Lieues sous les mers", verne, "9782070364234", "1870")
    print(livre_1)
    print(livre_2)
    print(livre_3)

    print("Création de 2 instances de Membre et affichage...")
    albert = Membre("EINSTEIN", "Albert", "14/03/1879")
    marie = Membre("CURIE", "Marie", "07/11/1867")
    print(albert)
    print(marie)

    print("\n*** 1er affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()
    print("\nEmprunts de livres...")
    albert.emprunter_livre(livre_1)
    albert.emprunter_livre(livre_2)
    marie.emprunter_livre(livre_2)
    print("\n*** 2ème affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()
    print("\nRestitution d'un livre...")
    albert.restituer_livre(livre_1)
    print("\n*** 3ème affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()
