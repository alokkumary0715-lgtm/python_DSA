"""onething behaving in many forms
types:-
1. Duck typing:- Meaning Python doesn't care about the object's type.

It only cares whether the object has the required method.

2.Method overridig:-
Method overriding happens when a child class provides its own implementation of a parent method
"""
#duck typing
class dog:
    def speak(self):
        print("bark")
                             #here python doesnt check its dog or cat it only checks .speak exist
class cat:
    def speak(self):
        print("meow")

def sound(ani):
        ani.speak()

sound(dog())
sound(cat())


class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()