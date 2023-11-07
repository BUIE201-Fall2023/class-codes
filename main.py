class Animal:
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("miyav")

class Dog(Animal):
    def talk(self):
        print("hav")

class Bird(Animal):
    def talk(self):
        print("cik")

c = Cat()
c.talk()

d = Dog()
d.talk()

# polymorphism
b = Bird()
pets = [c, d, b]
for pet in pets:
    pet.talk()
