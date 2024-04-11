# Define a class
class Person1:
    pass


person1 = Person1()
# Adding name attribute dynamically
person1.name = "John"
print(person1.name)


# Define instance attributes in the constructor
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person2("John", 25)
print(person.name)


# Define instance methods
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."


person = Person3("John", 25)
print(person.greet())


# Define class attributes
class Person4:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person4.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."


print(Person4.counter)
p1 = Person4("John", 25)
p2 = Person4("Jane", 22)
print(Person4.counter)


# Define class method
class Person5:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person5.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return Person5("Anonymous", 22)


anonymous = Person5.create_anonymous()
print(anonymous.name)


# Define static method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


f = TemperatureConverter.celsius_to_fahrenheit(30)
print(f)


# Single inheritance
class Employee1(Person5):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title


# Inheritance with overriding
class Employee2(Person5):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."


employee = Employee2("John", 25, "Python Developer")
print(employee.greet())
