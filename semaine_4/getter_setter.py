class Foo:

    def __init__(self, name):
        print("Initializing Foo...")
        self.name = name
        self._pays = None

    def set_pays(self, pays):
        # Mutateur
        self._pays = pays

    def get_pays(self):
        # Accesseur
        if self._pays is None:
            print("Le pays n'est pas défini.")
        return self._pays

f1 = Foo(    "Alice"     )
f1.set_pays("France")

print(f1._pays)