"""
==================================================
PYTHON OOPS - BASIC TO INTERMEDIATE REVISION
Single File Code for Quick Revision
Author: Prashant (Revision Purpose)
==================================================
"""

print("===== PYTHON OOPS REVISION STARTED =====\n")

# ==========================================================
# 1️⃣ CLASS & OBJECT
# Class = Blueprint
# Object = Instance of class
# ==========================================================

class Student:
    # Constructor (Automatically runs when object is created)
    def __init__(self, name, age):
        self.name = name      # Instance Variable
        self.age = age

    # Instance Method
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating Object
s1 = Student("Prashant", 21)
s1.introduce()

print("\n")


# ==========================================================
# 2️⃣ CLASS VARIABLE vs INSTANCE VARIABLE
# ==========================================================

class Employee:
    company = "Google"  # Class Variable (Shared by all objects)

    def __init__(self, name, salary):
        self.name = name      # Instance Variable
        self.salary = salary

e1 = Employee("Amit", 50000)
e2 = Employee("Rahul", 60000)

print("Company:", Employee.company)
print("Employee1:", e1.name, e1.salary)
print("Employee2:", e2.name, e2.salary)

print("\n")


# ==========================================================
# 3️⃣ TYPES OF METHODS
# Instance Method, Class Method, Static Method
# ==========================================================

class Demo:

    count = 0

    def __init__(self):
        Demo.count += 1

    # Instance Method
    def show_count_instance(self):
        print("Total objects:", Demo.count)

    # Class Method
    @classmethod
    def show_count_class(cls):
        print("Total objects (using class method):", cls.count)

    # Static Method
    @staticmethod
    def greet():
        print("Hello! This is a static method.")

d1 = Demo()
d2 = Demo()

d1.show_count_instance()
Demo.show_count_class()
Demo.greet()

print("\n")


# ==========================================================
# 4️⃣ ENCAPSULATION
# Using private variables
# ==========================================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# print(acc.__balance) ❌ Not accessible directly

print("\n")


# ==========================================================
# 5️⃣ INHERITANCE
# Child class inherits parent properties
# ==========================================================

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Inheriting from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Parent method
d.bark()   # Child method

print("\n")


# ==========================================================
# 6️⃣ TYPES OF INHERITANCE
# Single, Multiple, Multilevel
# ==========================================================

# Multilevel Inheritance
class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.house()
c.car()
c.bike()

print("\n")


# ==========================================================
# 7️⃣ METHOD OVERRIDING
# Child class redefines parent method
# ==========================================================

class Shape:
    def area(self):
        print("Area formula not defined")

class Circle(Shape):
    def area(self):
        print("Area = πr²")

sh = Shape()
cr = Circle()

sh.area()
cr.area()

print("\n")


# ==========================================================
# 8️⃣ POLYMORPHISM
# Same method name, different behavior
# ==========================================================

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

for animal in (Cat(), Cow()):
    animal.sound()

print("\n")


# ==========================================================
# 9️⃣ ABSTRACTION
# Using ABC (Abstract Base Class)
# ==========================================================

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

car = Car()
car.start()

print("\n")


# ==========================================================
# 🔟 MAGIC METHODS (Dunder Methods)
# Special built-in methods
# ==========================================================

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages."

b1 = Book("Python Basics", 250)
print(b1)  # Automatically calls __str__()

print("\n===== OOPS REVISION COMPLETED =====")
