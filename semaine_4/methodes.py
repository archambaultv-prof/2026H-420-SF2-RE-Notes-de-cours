class Bar:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Bar object with name '{self.name}' is being deleted.")

    def __str__(self):
        return f"{self.name}"

    def say_hello(self):
        print(f"Hello, {self.name}!")

    @staticmethod
    def say_goodbye():
        print("Goodbye!")

    @staticmethod
    def compare_bar_objects(bar1: 'Bar', bar2: 'Bar'):
        if bar1.name == bar2.name:
            print("The two Bar objects have the same name.")
        else:
            print("The two Bar objects have different names.")

b1 = Bar("Bob")
b2 = Bar("Charlie")

print(f"Avec mon object b1: {b1}")
print(f"Avec mon object b2: {b2}")

s_bad = b1.__str__()
s_good = f"{b1}"

# b1.say_hello()
# b2.say_hello()

# Bar.say_goodbye()
# b2.say_goodbye()