"""class person:
    __name=None
    __age=0
    def __init__(self,n,a):
        self.__name=n 
        self.__age=a

    def __setName(self,n):
            name =n

    def __setAge(self,a):
            age = a """



#task 1

"""studentname = None
marks = None

print("enter student name : ")
studentname = input("Name: ")
marks = int(input("marks:"))


if marks >= 80 and marks <= 100:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 50:
    grade = 'D'
else:
    grade = 'F'


print("student name : ", studentname)
print("marks : ", marks)
print("grade: ",grade) """



#task 2


"""num = None

print("enter number : ")
num = int(input())


for i in range (1,11):
    print(num," * ",i," = ",num*i) """


#task 3

"""num = None 
even_c =0
odd_c =0
print("enter 10 numbers : ")
for i in range(1,11):
    num = int(input())


    if num%2==0:
        even_c += 1
        print(num," is even")
    else:
        odd_c += 1
        print(num, "is odd")

print("total even = ",even_c)
print("total odd = ",odd_c) """

#task4

"""lst = []
while True:
        print("\nMenu:\n1. Add\n2. Remove\n3. Display\n4. Max/Min\n5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            val = int(input("Enter element: "))
            lst.append(val)
        elif choice == 2:
            val = int(input("Enter element to remove: "))
            if val in lst:
                lst.remove(val)
        elif choice == 3:
            print("List:", lst)
        elif choice == 4:
            if lst:
                print("Max:", max(lst), "Min:", min(lst))
            else:
                print("List is empty")
        elif choice == 5:
            break """

#task5:

"""def task5():
    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    unique = set(nums)
    print("Unique elements:", unique)

task5()"""

#task 6

"""class student:
    name = None
    rollno = None
    marks = None

    def __init__(self,n,r,m):
        self.name=n
        self.rollno=r
        self.marks=m

    def display(self):
        print("student name : ", self.name)
        print("student roll no : ", self.rollno)
        print("student marks : ", self.marks)

student1 = student("hasham",101,99)
student2 = student("ali",102,90)
student3 = student("junaid",103,91)


student1.display()
student2.display()
student3.display() """

#task7

"""class rectangle:
    length = None
    width = None

    def __init__(self,l,w):
        self.length=l
        self.width=w

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length+self.width)
    
r = rectangle(2.2,4)

print("area : ",r.area())
print("perimeter : ",r.perimeter()) """

#task8

"""class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("Balance:", self.__balance)

account = BankAccount()
account.deposit(100)
account.deposit(50)
account.withdraw(30)
account.display_balance() 
account.withdraw(200)      


#task9

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20


# Testing
emp = Employee("Ali", 50000)
mgr = Manager("Sara", 80000)

print(f"{emp.name}'s bonus: {emp.calculate_bonus()}")   
print(f"{mgr.name}'s bonus: {mgr.calculate_bonus()}")  


#task10

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started: Vroom Vroom!")


class Bike(Vehicle):
    def start(self):
        print("Bike started: Rrrm Rrrm!")


car = Car()
bike = Bike()

car.start()   
bike.start() 


#task11
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, company, salary):
        self.company = company
        self.salary = salary

    def details(self):
        print(f"Company: {self.company}, Salary: {self.salary}")

class Manager(Person, Employee):
    def __init__(self, name, age, company, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, company, salary)
        self.department = department

    def details(self):
        Person.details(self)
        Employee.details(self)
        print(f"Department: {self.department}")

mgr = Manager("Ali", 35, "TechCorp", 90000, "Engineering")
mgr.details() 


#task12

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2

print(v3) """

#task13

"""numbers = tuple(int(input(f"Enter number {i+1}: ")) for i in range(5))

print(f"\nMaximum : {max(numbers)}")
print(f"Minimum : {min(numbers)}")
print(f"Sum     : {sum(numbers)}") """

#task14

"""sentence = input("Enter a sentence: ").lower()

frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(f"{word}: {count}") 


#task15

students = {}

def add_student(name, marks):
    students[name] = marks
    print(f"{name} added!")

def update_marks(name, marks):
    if name in students:
        students[name] = marks
        print(f"{name}'s marks updated!")
    else:
        print(f"{name} not found!")

def display_all():
    for name, marks in students.items():
        print(f"{name}: {marks}")


add_student("Ali", 85)
add_student("Sara", 90)
add_student("Umar", 78)

update_marks("Ali", 95)
update_marks("Zara", 88)  # not found

print("\n--- All Students ---")
display_all()


#task16

import random

secret = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1

    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts!")
        break 

#task17

list1 = input("Enter first list  (space separated): ").split()
list2 = input("Enter second list (space separated): ").split()

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

print(f"Common elements: {common}") """


#task18

text = input("Enter a string: ").lower().replace(" ", "")

if text == text[::-1]:
    print(f"'{text}' is a Palindrome!")
else:
    print(f"'{text}' is NOT a Palindrome!") 


#task19
"""menu = {
    "apple": 50,
    "bread": 120,
    "milk": 80,
    "eggs": 200,
    "juice": 150
}

cart = []

def add_item(name):
    if name in menu:
        cart.append(name)
        print(f"{name} added to cart!")
    else:
        print(f"{name} not found in menu!")

def total_bill():
    total = sum(menu[item] for item in cart)
    print(f"Total Bill: Rs.{total}")

def display_cart():
    if cart:
        for item in cart:
            print(f"{item}: Rs.{menu[item]}")
    else:
        print("Cart is empty!")


add_item("apple")
add_item("milk")
add_item("juice")
add_item("pizza")   

print("\n--- Cart ---")
display_cart()

print()
total_bill() """


#task20

"""n = int(input("Enter a number: "))

if n < 2:
    print(f"{n} is NOT Prime!")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is NOT Prime!")
            break
    else:
        print(f"{n} is Prime!")


#task21

n = int(input("Enter number of students: "))

marks = [int(input(f"Enter marks of student {i+1}: ")) for i in range(n)]

print(f"\nAverage Marks : {sum(marks) / len(marks):.2f}")
print(f"Highest Marks : {max(marks)}")
print(f"Lowest Marks  : {min(marks)}") """