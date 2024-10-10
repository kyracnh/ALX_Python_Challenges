# Base Class
class Animal:
    # Method for eating
    def eat(self):
        print("The animal is eating.")
    
    # Method for sleeping
    def sleep(self):
        print("This animal is sleeping.")

# Subclass inheriting from Animal
class Dog(Animal):
    # Method specific to Dog class
    def bark(self):
        print("This dog is barking.")

animal = Animal()
animal.eat()
animal.sleep()

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()