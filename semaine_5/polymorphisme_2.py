# from abc import ABC, abstractmethod


class Eleve():
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        return f"Je suis {self.nom}, un élève."

    def __str__(self):
        return self.se_presenter()

# class ToString(ABC):
#     @abstractmethod
#     def __str__(self):
#         pass

e = Eleve("Charlie")
print(e)