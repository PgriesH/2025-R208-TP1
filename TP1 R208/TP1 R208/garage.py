from obj_voitures import Voitures

if __name__ == "__main__":
    car1 = Voitures("Renault", "Captur_TCE_90ch", 2018, 7.2, "Gris foncé", 20000)
    print(car1)
    car2 = Voitures("Renault", "Clio_TCE_100ch", 2018, 5.5, "Bleu nuit", 17000)
    print(car2)
    print(car1.calcul_consommation(1060))
    print(car2.calcul_consommation(1060))
    print(car1.calcul_prix(1060))
    print(car2.calcul_prix(1060))
    print(car1.modif_prix_litre(1060))
    print(car2.modif_prix_litre(1060))
