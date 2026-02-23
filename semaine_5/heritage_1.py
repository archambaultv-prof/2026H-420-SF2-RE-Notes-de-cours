class Parent:
    def __init__(self, name):
        self.name = name
        self.attribut = None

    def set_attribut(self, attribut):
        self.attribut = attribut

    def greet(self):
        return f"Hello, I am {self.name}."

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        raise NotImplementedError("La méthode greet doit être implémentée dans la classe Child.")

p = Parent("Alice")
c = Child("Bob", 10)

print(p.greet()) 
print(c.greet())