class Voitures():
    # Constructeur avec 3 arguments...
    def __init__(self, marque = "Ferrari", modele = "SF90_spider", annee = 2010):
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"


if __name__ == "__main__":
    # Création d’une instance...
    car = Voitures("Renault", "Clio", 2018)
    # Lecture d’un attribut d’instance...
    caisse = car.modele
    # Affichage...
    print(car)
    # Ecriture (modification) d’un attribut d’instance...
    car.annee = 2020
    # Affichage encore...
    print(car)

    car2 = Voitures("Peugot", "208", 2019)
    print(car2)
    car3 = Voitures("Ford", "Mustang")
    print(car3)
    car4 = Voitures()
    print(car4)
    car5 = Voitures("F40")
    print(car5)
    voiture6 = Voitures(modele="296_GTS")
    print(voiture6)
    print(type(voiture6))
    print(vars(voiture6))

