age = 30
nom = "Alice"
travail = "Exploratrice"

def se_presenter(nom, age, travail):
    return f"Bonjour, je m'appelle {nom}, j'ai {age} ans et je suis {travail}."

def est_majeur(age):
    return age >= 18

def se_presenter_v2(nom, age, travail):
    return f"Bonjour, je m'appelle {nom}, j'ai {age} ans et je suis {travail} !!!!"

# print(se_presenter)

# Version avec une liste

AGE = 1
NOM = 2
TRAVAIL = 3
SE_PRESENTER = 4
EST_MAJEUR = 5

alice = [None, 30, "Alice", "Exploratrice", se_presenter, est_majeur]
bob = [None, 25, "Bob", "Ingénieur", se_presenter, est_majeur]
henry = [None, 17, "Henry", "Étudiant", se_presenter, est_majeur]

# Heritage avec une liste
PARENT = 0

# Une autre "classe" sous forme de liste : etudiant
ECOLE = 1
MOYENNE = 2

jacques = [[None, 18, "Jacques", "TUTEUR", se_presenter, est_majeur], "College de Maisonneuve", 82]

print(jacques[PARENT][NOM])

# Version avec une classe

# class Personne:
#     def __init__(self, nom, age, travail):
#         self.nom = nom
#         self.age = age
#         self.travail = travail

#     def se_presenter(self):
#         return f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans et je suis {self.travail}."

#     def est_majeur(self):
#         return self.age >= 18

# alice_classe = Personne("Alice", 30, "Exploratrice")
# print(dir(alice_classe))
# classe_de_alice = alice_classe.__class__

# # possede_methode_se_presenter = "se_presenter" in dir(alice_classe)
# possede_methode_se_presenter = hasattr(alice_classe, "se_presenter")
# print(possede_methode_se_presenter)