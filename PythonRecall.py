#Variables
a = 10
b = 20.5
c = "Hello, World!"
d = True
e = [1, 2, 3, 4, 5]
f = (6, 7, 8, 9, 10)
g = {11, 12, 13, 14, 15}
h = {'name': 'Alice', 'age': 30}

#Print statemets
print("Integer:", a)
print(f"Float: {b}")
print("Hello, World!")

#classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Athlete:
    def __init__(self, name, sport, number):
        self.name = name
        self.sport = sport
        self.number = number

    def introduce(self):
        return f"I am {self.name} and I play {self.sport}."
    def get_number(self):
        return f"My jersey number is {self.number}."
    
person = Person("Alice", 30)
print(person.greet())
athlete = Athlete("Bob", "Soccer", 10)
print(athlete.introduce())
print(athlete.get_number())

#conditional statements
if a < b:
    print(f"{a} is less than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is greater than {b}")

#functions
def addition():
    sum = a+b
    return sum
print("Sum:", addition())

#loops
for i in e:
    print("List item:", i)
for j in f:
    print("Tuple item:", j)

for j in range(5):
    print("Range item:", j)

count = 0
while count < 5:
    print("Count:", count)
    count += 1

#Exception handling
try:
    result = a / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")
    
#recursion, need base case
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

#list comprehension
squared = [x**2 for x in e]
print("Squared list:", squared)

#lambda functions
multiply = lambda x, y: x * y
print("Multiplication using lambda:", multiply(5, 10))