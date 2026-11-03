from exam import *

a = "ab"
b = "aa"

print(a > b)  # This will print True because "ab" is greater than "aa" in lexicographical order.

x, y = symbols('x y')

num = {'0': '0\n1\n2\n3'}

print(num['0'], end=" ")
print("\rhello")

c = 0
def cheese(c):
    return c + 2
print(cheese(c))

def milk(a = 10, b = 2):
    return a + b

print(milk(3))
print(milk(b = 5))

def cereal(a, b = "Oats", c = "cheese"):
    print(a, b, c)

cereal("marshmallow", c = "milk")

def outside():
    name = "Alice"
    print(name)

    def inside():
        nonlocal name
        name = "Bob"
        print(name)

myStr = "hi"
myList = [1, 2]
myTuple = (myStr, myList)
print(myTuple)
myStr = "hello"
myList[0] = 5
print(myTuple)

list = ["hello:123", "world:456"]
list2 = [item.split(":") for item in list]
print(list2)