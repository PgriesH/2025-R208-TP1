class Voitures():
    prix_litre = 1.70

    # Constructeur avec 3 arguments...
    def __init__(self, marque, modele, annee, conso=6.0, couleur="Blanc", prix="None"):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.conso = conso
        self.couleur = couleur
        self.prix = prix

    def calcul_consommation(self, distance):
        litres = distance * 100 / self.conso
        return litres

    def calcul_prix(self, distance):
        prixtrajet = (distance * 100 / self.conso) * Voitures.prix_litre
        return prixtrajet

    def modif_prix_litre(self, distance):
        Voitures.prix_litre = Voitures.prix_litre + 1
        prixtrajet = (distance * 100 / self.conso) * Voitures.prix_litre
        return prixtrajet

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture : {self.marque} : {self.modele} - {self.annee} - {self.couleur} - {self.conso}l/100km - {self.prix}"
