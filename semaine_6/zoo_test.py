class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Animal({self.name})"

t = Animal("Tigre")
ls = [Animal("Lion"),t, Animal("Ours")]
print(ls)

ls.remove(Animal("Tigre"))
print(ls)