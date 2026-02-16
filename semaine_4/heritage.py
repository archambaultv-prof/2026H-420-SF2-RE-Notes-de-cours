class Livre:
    def __init__(self, titre, auteur, annee):
        print("Constructeur de Livre appelé")
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        return f"{self.titre} de {self.auteur} ({self.annee})"

    def nouveaute(self):
        return self.annee > 2024

class Roman(Livre):
    def __init__(self, titre, auteur, annee):
        print("Constructeur de Roman appelé")
        super().__init__(titre, auteur, annee)

class BandeDessinee(Livre):
    def __init__(self, titre, auteur, annee, dessinateur):
        print("Constructeur de BandeDessinee appelé")
        super().__init__(titre, auteur, annee)
        self.dessinateur = dessinateur

    def __str__(self):
        return f"{self.titre} de {self.auteur} ({self.annee}), dessiné par {self.dessinateur}"

r = Roman("Le Comte de Monte-Cristo", "Alexandre Dumas", 1844)
bd = BandeDessinee("Asterix le Gaulois", "René Goscinny", 1961, "Albert Uderzo")

print(r)
print(bd)