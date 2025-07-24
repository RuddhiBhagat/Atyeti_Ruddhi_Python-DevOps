#What happens when you perform operations between different data types
# like int + bool or str * float? Why?

# int + bool
print(5 + True)   # Output: 6
print(5 + False)  # Output: 5

'''In python,boolean is subclass of int.
True is treated as 1 and False as 0.'''


# str *  float

print("abc" * 2.5)  # TypeError
'''Python does not allow multiplying a string by a float.
Only integers are valid repeat counts for strings.
Python is strongly typed (it doesn’t auto-convert types when it shouldn't).
It is also dynamically typed (it figures out types at runtime), but you still need valid type combinations.'''

#Explain how Python internally handles memory allocation for immutable vs mutable data types.

#---Immutable types (int, float, str, tuple).
#---Their value cannot be changed once created.

x = 5
print(id(x))   # Memory ID of 5
x += 1
print(id(x))   # New memory ID (different object)

#---Mutable types (list, dict, set):
#---You can change their contents without changing their memory location.

l = [1, 2]
print(id(l))
l.append(3)
print(id(l))  # Same ID

#-------------------------------------------------------------


#What are some potential issues when using is vs == while comparing variables? Give examples.

#== checks value equality.
#is checks identity (same memory location).

a = [1, 2]
b = [1, 2]
print(a == b)  # True (same value)
print(a is b)  # False (different objects)

x = 256
y = 256
print(x is y)  # True (Python interns small integers)

x = 300
y = 300
print(x is y)  # False (may not be interned)

#-------------------------------------------------------------

#How does Python's dynamic typing system handle function arguments and return types? What are potential downsides?

#---Python doesn't require specifying argument/return types:

def add(a, b):
    return a + b
print(add(1, 2))      # 3
print(add("a", "b"))  # "ab"

#Dynamic typing allows flexibility but also:
#Increases the risk of runtime errors.
#Makes debugging and maintenance harder in large codebases.

#Solution:
#Use type hints:
def add(a: int, b: int) -> int:
    return a + b

#-------------------------------------------------------------

#How can you check the type of a variable at runtime and dynamically enforce a specific type?

#Runtime Type Checking:
x = 42
print(type(x))             # <class 'int'>
print(isinstance(x, int))  # True

#Enforce Type Dynamically:
def process(value):
    if not isinstance(value, int):
        raise TypeError("Expected an int")
    return value * 2

print(process(5))  # OK
print(process("hi"))  # TypeError
