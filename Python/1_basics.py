# Variables and Data Types
x = 10               # Integer
y = 3.14             # Float
name = "John"        # String
is_student = True    # Boolean

# Lists
numbers = [1, 2, 3, 4, 5]       # List
fruits = ['apple', 'banana', 'cherry'] # List

# Tuples
coordinates = (10, 20)          # Tuple

# Dictionaries
person = {'name': 'John', 'age': 30}  # Dictionary

# Control Flow
# If statement
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# For loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1


# Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# Modules and Libraries
import math

print(math.sqrt(16))  # Square root function from the math module


# Object-Oriented Programming
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# Creating an object
person1 = Person("John", 30)
person1.greet()


# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Generators
def square_numbers(nums):
    for num in nums:
        yield num * num

my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Concurrency and Threading
import threading

def print_numbers():
    for i in range(5):
        print(i)

# Create a thread
thread = threading.Thread(target=print_numbers)
# Start the thread
thread.start()

# Regular Expressions
import re

pattern = r'\b\w{4}\b'  # Match 4-letter words
text = "Python is an amazing language abcd"
matches = re.findall(pattern, text)
print(matches)


# Lambda Functions and Higher-Order Functions
# Lambda function
add = lambda x, y: x + y
print(add(5, 3))

# Higher-order function
def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(lambda x, y: x * y, 5, 3)
print(result)

# List Comprehensions and Generator Expressions
# List comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

# Generator expression
even_numbers = (x for x in range(10) if x % 2 == 0)
print(list(even_numbers))

# Asynchronous Programming
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(say_hello())


