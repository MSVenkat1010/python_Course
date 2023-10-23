myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
'''
The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
'''
mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

#Mixing operators between numbers and strings is not supported
"""
This will not work!
one = 1
two = 2
hello = "hello"
#print(one + two + hello)
it will give type error
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

"""
output:
7
7.0
7.0
hello
hello
Don't worry about apostrophes
3
hello world
3 4
String: hello
Float: 10.000000
Integer: 20
"""