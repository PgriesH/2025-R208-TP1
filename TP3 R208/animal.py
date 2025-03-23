class Animal:
    def __init__(self, nom, age, style, titre):
        self.nom = nom
        self.age = age
        super().__init__(style, titre)

    def se_presenter(self):
        super().se_presenter()
        print(f"\t\tJe me nomme {self.nom}, j'ai {self.age} ans.")


class Mammifere(Animal):
    def __init__(self, nom, age, race, type_pelage, couleur, style, titre):
        super().__init__(nom, age, style, titre)
        self.race = race
        self.type_pelage = type_pelage
        self.couleur = couleur

    def se_presenter(self):
        print(f"Je suis un(e) {self.race} revêtu de {self.type_pelage} de couleur : {self.couleur}.")
        super().se_presenter()


class Oiseau(Animal):
    def __init__(self, nom, age, ordre, envergure, style, titre):
        super().__init__(nom, age, style, titre)
        self.ordre = ordre
        self.envergure = envergure

    def se_presenter(self):
        print(f"Je suis un oiseau de type {self.ordre} et mon envergure est de {self.envergure} cm.")
        super().se_presenter()


class Personnage:
    def __init__(self, style, titre):
        self.style = style
        self.titre = titre

    def se_presenter(self):
        print(f"\tJe joue dans le {self.style} : {self.titre}.")


class ActeurMammifere(Mammifere, Personnage):
    def __init__(self, nom, age, race, type_pelage, couleur, style, titre):
        super().__init__(nom, age, race, type_pelage, couleur, style, titre)


class ActeurOiseau(Oiseau, Personnage):
    def __init__(self, nom, age, ordre, envergure, style, titre):
        super().__init__(nom, age, ordre, envergure, style, titre)


if __name__ == "__main__":
    animaux = [
        ActeurMammifere("Simba", 5, "lion", "poils courts", "fauve clair", "dessin animé", "Le livre de la jungle"),
        ActeurMammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve", "film", "Beethoven"),
        ActeurMammifere("César", 26, "singe", "poils courts", "marron", "film", "La planète des singes"),
        ActeurMammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise", "dessin animé", "Dumbo"),
        ActeurOiseau("Hedwige", 7, "rapace", 90, "film", "Harry Potter"),
        ActeurOiseau("Blu", 5, "perroquet", 100, "dessin animé", "Rio"),
        ActeurOiseau("Lago", 12, "perroquet", 60, "film", "Aladin"),
        ActeurOiseau("Zazu", 40, "passereau", 0, "dessin animé", "Le roi lion"),
    ]
    print(f"MRO de ActeurMammifere : {ActeurMammifere.mro()}")
    print(f"MRO de ActeurOiseau : {ActeurOiseau.mro()}")
    print()
    for animal in animaux:
        animal.se_presenter()
    print()
