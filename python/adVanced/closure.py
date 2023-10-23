"""
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step

Firstly, a Nested Function is a function defined inside another function.
It's very important to note that the nested functions can access the variables of the enclosing scope. 
However, at least in python, they are only readonly.
However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.
"""
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"),"=>check")

def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
print(transmit_to_space("Burn the Sun!"))

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=4
        print(number)
    printer()
    print(number)

print_msg(9)

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
"""
OutPut:
Test message
None =>check
Burn the Sun!
<function transmit_to_space.<locals>.data_transmitter at 0x100eacb80>
4
4
45
"""



