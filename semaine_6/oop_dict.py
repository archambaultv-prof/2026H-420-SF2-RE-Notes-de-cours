def se_presenter(nom, age, travail):
    return f"Bonjour, je m'appelle {nom}, j'ai {age} ans et je suis {travail}."

def est_majeur(age):
    return age >= 18


# print(se_presenter)

# Version avec une dictionnaire

# AGE = 1
# NOM = 2
# TRAVAIL = 3
# SE_PRESENTER = 4
# EST_MAJEUR = 5

alice = {"nom": "Alice", "age": 30, "travail": "Exploratrice", "se_presenter": se_presenter, "est_majeur": est_majeur}
bob = {"nom": "Bob", "age": 25, "travail": "Ingénieur", "se_presenter": se_presenter, "est_majeur": est_majeur}
henry = {"nom": "Henry", "age": 17, "travail": "Étudiant", "se_presenter": se_presenter, "est_majeur": est_majeur}

# # Heritage avec une liste
# PARENT = 0

# # Une autre "classe" sous forme de liste : etudiant
# ECOLE = 1
# MOYENNE = 2

def presenter_jacques():
    return "Yo !"

jacques = {"parent": {"nom": "Jacques", "age": 18, "travail": "TUTEUR", "se_presenter": se_presenter, 
                      "est_majeur": est_majeur}, 
            "ecole": "College de Maisonneuve",
            "se_presenter": presenter_jacques,
            "moyenne": 82}

def appelle_methode_ou_attribut(obj, nom):
    if nom in obj:
        methode = obj[nom]
        print(methode)
    elif "parent" in obj and nom in obj["parent"]:
        methode = obj["parent"][nom]
        print(methode)
    else:
        print(f"Erreur: la méthode {nom} n'existe pas pour cet objet.")

appelle_methode_ou_attribut(jacques, "se_presenter")


# Polymorphisme

chien = {"nom": "Rex"}

appelle_methode_ou_attribut(chien, "nom")
appelle_methode_ou_attribut(jacques, "nom")





jacques = {"parent": {"nom": "Jacques", "age": 18, "travail": "TUTEUR", "se_presenter": se_presenter, 
                      "est_majeur": est_majeur}, 
            "ecole": "College de Maisonneuve",
            "se_presenter": presenter_jacques,
            "moyenne": 82}

class Personne:
    def __init__(self, nom, age, travail):
        self.nom = nom
        self.age = age
        self.travail = travail

    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans et je suis {self.travail}."

    def est_majeur(self):
        return self.age >= 18

class Etudiant(Personne):
    def __init__(self, nom, age, travail, ecole, moyenne):
        super().__init__(nom, age, travail)
        self.ecole = ecole
        self.moyenne = moyenne
    
    def se_presenter(self):
        s = super().se_presenter()
        return f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans, je suis {self.travail} et j'étudie au {self.ecole} avec une moyenne de {self.moyenne}."