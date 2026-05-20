from abc import abstractmethod, ABC

class MonException(Exception):
    pass

class Abstraite(ABC):
    
    @abstractmethod
    def ma_methode_abstraite(self, p1) -> str:
        pass

    def une_methode_avec_code_par_default(self):
        return "Le code par defaut"


class Foo(Abstraite):
    def __init__(self, p1: str, p2: int):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "Ma super classe Foo"

    def ma_methode(self, p1, p2):
        return p1 + p2

    def ma_methode_abstraite(self, p1):
        return "Pas de Kaboom !"
    
    def une_methode_avec_code_par_default(self):
        raise MonException("Ha ha, dans ta face !")

    
if __name__ == "__main__":
    print("Un deux trois test")
    f = Foo("Foo", 2)
    print(f)