#Object Oriented Programming

#Class
#Example 1 car
class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
         print("Engine started")

    def stop_engine(self):
        print("Engine stopped")
my_car=car("Toyota","Corola",2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

                #Bank Acconut
           
         #Example 3: Rectangle
class Rectangle:
    def __init__(self,length,width):
      self.length = length
      self.width = width

    def calculate_area(self):
                     return self.length * self.width
                 
    def calculate_perimeter(self):
                     return 2*(self.length*self.width)
                 #create a rectangle
my_rectangle=Rectangle(15,5)
print(my_rectangle.length)
print(my_rectangle.width)
                 #calculate and display the area and perimeter
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())
                                         
                           
    #Convert temperature 37celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function with 37 degrees Celsius
celsius = 37
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


#Exercise
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def give_pay_increment(self, increment_amount):
        self._salary += increment_amount


# Create an instance of Employee
employee = Employee("Gafabusa Willy", 850000)

# Get the employee's current salary
current_salary = employee.get_salary()
print(f"Current salary of {employee.get_name()}: {current_salary} Ugx")

# Give a pay increment of 150,000 Ugx
increment_amount = 150000
employee.give_pay_increment(increment_amount)

# Get the updated salary
new_salary = employee.get_salary()
print(f"New salary of {employee.get_name()}: {new_salary} Ugx")

#Inheritance
class Animal:
      def __init__(self,name,age):
            self._name = name

      def eat(self):
       print(f"[self.name] is eating")

       class Dog(Animal):
            def bark(self):
                 print(f"{self.name} is meowing")

                 class Cat(Animal):
                      def meow(self):
                           print(f"{self.name} is meowing")

                 #create animal objetcs
                 animal=Animal("Generic Animal")
                 dog=Dog("Spot")
                 cat=Cat("Fluffy")

                 #invoke call eat method
                 animal.eat()
                 dog.eat()
                 cat.eat()
                 cat.meow()

#Exercise calculating the area of a circle and perimeter of a rectangle
import math
from typing import Any

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

# Example usage
radius = 5.0
circle = Circle(radius)
circle_area = circle.calculate_area()
print(f"The area of the circle with radius {radius} is {circle_area}")

#Exercise: calculate the perimeter of a rectangle using inheritance
class Shape:
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

# Example usage
length = 4.0
width = 6.0
rectangle = Rectangle(length, width)
rectangle_perimeter = rectangle.calculate_perimeter()
print(f"The perimeter of the rectangle with length {length} and width {width} is {rectangle_perimeter}")

#Multiple inheritance
class Animal:
    def __init__(self, name):
        self._name = name
    def eat(self):
        print(f"[self.name] is eating")
class Flyable:
    def fly(self):
        print(f"[self.name] is flying")
class Bird(Animal,Flyable):
    def __init__(self, name,species):
        super().__init__(name)
        self._species = species

    def display_info(self):

     print(f"species: {self.species}")
     print(f"name: {self._name}")

          #create bird object
my_bird=Bird("Pigeon","bird")
my_bird.eat()
my_bird.fly()

          #Method overriding
class Animal:
    def make_sound(self):
        print("Animal is making a sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")
def make_animal_sound(animal):
             animal.make_sound()
               #create objects
animal=Animal()
dog=Dog()
cat=Cat()

          #calling make_animal_sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)
          
          #POLYMORPHISM
class Shape:
    def calculate_area(self):
          pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
          return self.length*self.width
    
class Circle(Shape): 
    def __init__(self,radius):
         self.radius=radius
    def calculate_area(self):
          return 3.14 * self.radius**2
    def calculate_circumference(self):
          return 2*3.14*self.radius
     
     #create objects
    rectangle=Rectangle(15,5)
    circle=Circle(5)

     #Display area
    print("Rectangle Area: ", rectangle.calculate_area())
    print("Circle area is:", circle.calculate_area())
            
    #Abstraction
      
     
               
                        
        

            

















            
