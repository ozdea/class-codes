# abstract class
class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Hav")

class Cat(Animal):
    def talk(self):
        print("Miyav")

class Bird(Animal):
    def talk(self):
        print("Cik")

cat = Cat()
bird = Bird()
bird2 = Bird()
dog = Dog()

pets = [cat, bird, bird2, dog]

def all_talk(pets):
    for pet in pets:
        pet.talk()

all_talk(pets)