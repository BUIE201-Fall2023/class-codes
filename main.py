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

i = 5
print(type(i)) #int

my_bool = True
print(type(my_bool)) #bool
print("issubclass(bool, int)", issubclass(bool, int))

my_float = 3.41
print(type(my_float)) #float
print("issubclass(int, float)", issubclass(int, float))

my_int = int(my_float)

print(type(d)) #dog
print(type(b)) #bird

print("issubclass(Bird, Animal)", issubclass(Bird, Animal))

print("issubclass(int, object)", issubclass(int, object))
print("issubclass(float, object)", issubclass(float, object))
print("issubclass(Animal, object)", issubclass(Animal, object))
