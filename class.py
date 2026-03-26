class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def instroduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


nhat = Person("Nhat", 20)
nhat.instroduce()

print(nhat)