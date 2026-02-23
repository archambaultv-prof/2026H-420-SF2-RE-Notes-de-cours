# from abc import ABC, abstractmethod


# class ChoseQuiAvance(ABC):

#     @abstractmethod
#     def avancer(self) -> None:
#         pass

class Cheval():
    def __init__(self, nom):
        self.nom = nom

    def avancer(self):
        print(f"{self.nom} galope.")

class Voiture():
    def __init__(self, marque):
        self.marque = marque

    def avancer(self):
        print(f"La {self.marque} roule.")

c = Cheval("Spirit")
v = Voiture("Toyota")

choses_qui_avancent = [c, v]
choses_qui_avancent2 = [v, c]

for chose in choses_qui_avancent:
    chose.avancer()
    if isinstance(chose, Cheval):
        print("Howdy, partner!")