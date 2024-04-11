class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Bho bho!")

    def print_info(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def celebrate_birthday(self):
        self.age += 1


bruno = Dog("Bruno", 2)
bruno.print_info()
bruno.bark()
print()

cuddles = Dog("Cuddles", 1)
cuddles.print_info()
cuddles.bark()
cuddles.celebrate_birthday()
cuddles.print_info()
