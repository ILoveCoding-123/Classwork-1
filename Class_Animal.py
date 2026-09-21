from abc import ABC, abstractmethod

class Animal(ABC):


    def move(self):

        pass

class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can slither")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

class Bird(Animal):

    def move(self):
        print("I can fly")

class Fish(Animal):

    def move(self):
        print("I can swim")

class Cow(Animal):

    def move(self):
        print("I can moo")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()

B = Bird()
B.move()

F = Fish()
F.move()

C = Cow()
C.move()
