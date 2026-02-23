from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def faire_bruit(self) -> str:
        pass

class Chat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def retomber_sur_ces_pattes(self):
        return f"{self.name} retombe sur ses pattes."

    def faire_bruit(self):
        return "Meow!"

class Chien(Animal):
    def __init__(self, name):
        super().__init__(name)

    def faire_bruit(self):
        return "Woof!"

liste_animaux = [Chat("Whiskers"), Chien("Rex")] #, Animal("Alpha")]
for animal in liste_animaux:
    print(f"{animal.name} dit: {animal.faire_bruit()}")
