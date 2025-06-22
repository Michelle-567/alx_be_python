# class Animal:
#   def make_sound(self):
#     print("Generic animal sound")

# class Dog(Animal):
#   def make_sound(self):
#     print("Woof!")
class Duck:
    def quack(self):
        print("Duck quacks") 

class Person:
    def quack(self):
        print("Person imitates duck") 

animals = [Duck(), Person()]
for animal in animals:
  animal.quack()
  

#   Single Inheritance Instruction:

# Create a base class Shape with a method calculate_area().
# Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle.
class Shape:
    def calculate_area(self, L):
        area = L * L
        return(area)
        
class Rectangle(Shape):
    def calculate_area(self, W, L):
        area = L * W
        return(area)

# Multiple Inheritance Instruction:

# Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
# Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods         
class Bird:
    def fly(self):
        print("flying")

class Mammal:
    def run(self):
        print("running")   

class Bat(Bird, Mammal):
    def fly(self):
        print("A bat flys")
    def run(self):
        print("A bat runs")

# class Bat(Bird,Mammal):
#     def run(self):
#         return super().run()
    
#     def fly(self):
#         return super().fly()


# Animal=Bat()
# Animal.fly()
# Animal.run()

# Polymorphism with Duck Typing Instruction:

# Create classes Dog, Cat, and Bird, each with a method make_sound().
# Implement different behaviors for make_sound() in each class.
# Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.
class Dog:
    def make_sound(self):
        print ("barks")
    
class Cat:
    def make_sound(self):
        print ("meows")
    
class Bird:
    def make_sound(self):
        print ("chirps")

obj1 = Dog()
obj2 = Cat()
obj3 = Bird()

my_objs = [obj1, obj2, obj3]
def let_them_speak(my_objs):
    for obj in my_objs:
        obj.make_sound()
     
let_them_speak(my_objs)
