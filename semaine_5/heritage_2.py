class Parent:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return f"{self.nom} dit : Bonjour !"

class Enfant(Parent):
    pass

e = Enfant("Alice")
print(e.parler())