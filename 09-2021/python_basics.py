#Print command
print("value") #prints the value that was given.

#Variables
x = "Mark" #THIS IS A STRING
y = 22 #this is an integer
z = 12,4444444 #this is a float

print("i am " + x + " i am" + y + " year old\nI will become "+ x+1 +" in"+ z +" days")#\n makes a new line.
print(f"{x}, {y}, {z}") #prints the variables using a fstring
print("%s + %d + %.2f"(x,y,z))#prints the variables with %(valuetype) and we can manipulate it with the point key

#input
x = input("geef een getal: ")
x, y = input("geef 2 getallen seperated with a period: ").split(",")

#functions
def func_name(x,y):
    #function line
#calling a function
func_name(num1,num2)

#if-statement
a = 3
b = 5

if a > b:
    print("yes")
elif a == b:
    print("no")
else:
    print("maybe")

#loops

#WHile loops repeat there block until it is false
#this is a infinite loop
condition = True
while condition == True:
    print("True")
    #makes the infinite loop finite
    condition = False
count = 0
while count < 10:
    print("True")
    count = count +1
print("False")

#for loop does the block in a predetermined amount of times
items = [1, 2, 3, 4]
for item in items:
    print(item)
#or
for item in range(15):
    print(item)
#enumerate get the index and the item of the list
for index, item in enumerate(items):
    print(item)

#break and continue
#break breaks the loop and does the following code after the loop
#continue skips a line in the loop

#this is a LIST
x = ['hi', 'hello', 'welcome']
print(x[1])

#this is a DICTIONARY
# uses key:value
ages = { 'Mark': 22,
         'Tynka': 18,
         'Pablo': 5 }
print(ages['Mark'])

#DIC FUNC
nums = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in  nums) #gives True
print("three" in nums) # gives False because only keys can be used for 'in' 
print(4 not in nums) # gives True

#You can check if a key is in a dic:
if x in dic:
    print("yes")

#FUNC get

pairs = {
   1: "apple",
   "orange": [2, 3, 4], 
   True: False, 
   12: "True",
}
print(pairs.get("orange")) #gives value of key, otherwise gives none
print(pairs.get(7, 42))#gives 42 because 7 is not there
print(pairs.get(12345, "not found"))# gives not found because first value wasnt found
#See countries.py

#TUPLES --> similar to list but you cant change them (immutable)
words = ("spam", "eggs", "sausages") #uses parentheses ()
print(words[0])
#OR
my_tuple = "one", "two", "three"
print(my_tuple[0])
#Tuple unpacking
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c) #c will get assigned the values 3 to 8., it will give [3,4,5,6,7,8]
print(d)

#SETS
#sets are unorder therefore cannot be indexed
num_set = {1, 2, 3, 4, 5}
print(3 in num_set)# gives True

#add , remove and len function

nums = {1, 2, 1, 3, 1, 4, 5, 6} #sets cant contain duplicates so they get removed
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
print(len(nums))


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
#sets can be combined using math op
"""
The union operator | combines two sets to form a new one containing items in either. 

The intersection operator & gets items only in both. 

The difference operator - gets items in the first set but not in the second. 

The symmetric difference operator ^ gets items in either set, but not both. 
"""
print(first | second)#{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second)#{4, 5, 6}
print(first - second)#{1, 2, 3}
print(second - first)#{8, 9, 7}
print(first ^ second)#{1, 2, 3, 7, 8, 9}

#List comperhensions = way of quickly making lists
cubes = [i**3 for i in range(5)]

print(cubes)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

nums = (55, 44, 33, 22)
print(max((min(nums[:2])), abs(-42)))#[:2] gives the first 2 values of the tuple

"""
When to use a dictionary:
- When you need a logical association between a key:value pair.

- When you need fast lookup for your data, based on a custom key.

- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.

- Use a set if you need uniqueness for the elements. 

- Use tuples when your data cannot/should not change.
"""
#classes
class Animal:
    def walk(self):
        print("walking....")
#by adding animal in dog class it inherits the animal functions
class Dog(Animal):

    #init class is a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof")

roger = Dog("roger", 8)
print(type(roger))#gives dog class
print(roger.name)#gives name
print(roger.age)#gives age
roger.bark()#gives woof
roger.walk()#gives walking...

#modules
#you can add functions from other files if you import (name of file)
#or from (file name) import (function)
#if you add a python file with __init__.py in a folder it will say to python that folder contains modules

#argument from command line
import sys

print(sys.argv)#prints the list of argument gotten in the CLI

#accepting arguments
import argparse

parser = argparse.ArgumentParser(
    description='this program prints the name of my dogs'
)
parser.add_argument('-c', '--color', metavar='color',
choices={'red', 'yellow'}, required=True, help='the color to search for')

args = parser.parse_args()

print(args.color)#in CLI type python (file name) -c (a color)
#this will output the color given in the CLI

# lambda functions
#just doubles the value of the number
lambda num : num * 2

mulitply = lambda a, b : a * b

print(mulitply(2, 4))#will give 8

#map(), filter() and reduce()
numbers = [1, 2, 3, 4, 5, 6]
#map maps over the existing list creating a new one
def double(a):
    return a * 2
#or
double = lambda a: a*2
#or
result = map(lambda a: a*2, numbers)#more simplified
#map gives map object back

result = map(double, numbers)
print(list(result))
#filter filters the list, doesnt show values not used in the list,  creates new list
def isEven(n):
    return n % 2 == 0
#or
lambda n : n % 2 == 0
result = filter(isEven, numbers)

print(list(result))

#reduce used to calculate a value out of a sequence for example a list:
from functools import reduce
expenses = [
    ('dinner', 80)
    ('car repair', 120)
]

#sum = 0
#for expense in expenses:
#    sum += expense[1]

sum = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum)

#recursion
def factorial(n):
    #if u use recursion always have a check when it needs to exit the recursive line
    if n == 1: return 1
    return n * factorial(n-1)

#decorators
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper
@logtime
def hello():
    print("hello")

hello()#ouput is: before\n hello\n after

#docstrings
"""explain your code"""

#annotations
#specifying what a value will be or what a functions receives
def increment(n : int) -> int:
    return n + 1
count: int = 0

#exceptions

try:
    #some line of code
except <error1>: #the error has to be a specific error e.g. EOFError end of file error
    #handler <error1>
except <error2>:
    #handler <error2>
except:

else: # if no error occurs

finally:
    #do something in any case

#raise can raise your own exceptions
raise Exception('an error!')

class NotFoundException(Exception):
    pass

try:
    raise NotFoundException()
except NotFoundException:
    print("exception found")

filename = '/Users/xxxxxxx'
with open(filename, 'r') as file:
    content = file.read()
    print(content)

#list compression

numbers = [1, 2, 3, 4, 5]
#list compression syntax, used ofr simple lines
numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

#or
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
#or
numbers_power_2 = list(map(lambda n : n**2, numbers))

#polymorphism
#if you have 2 classes with the same function you can call them both even if its the same

#Operator overloading
#in class
#is the greaterthan function and compares from classes
def __gt__(self, other):
    return True if self.age > other.age else False
#then for ex print(roger > syd)


#OOP -> classes and objects

# What is an object?
#Every data type is a class and if u asign a value to somethings its a object

#methods -> you can perform these on objects