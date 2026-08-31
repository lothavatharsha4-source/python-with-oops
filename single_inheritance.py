class animal:
    def eat(self):
        print("animal is eating")

    def barking(self):
        print("animal is barking")

class dog(animal):
    def sound(self):
        print("dog is barking")

d1 = dog()
d1.eat()
d1.barking()
d1.sound()