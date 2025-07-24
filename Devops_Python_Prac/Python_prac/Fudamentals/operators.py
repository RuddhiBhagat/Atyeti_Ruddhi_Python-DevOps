#How does Python handle operator precedence and associativity with chained comparisons like 3 < 5 == True?

#---Python allows chained comparisons, and they are evaluated differently than most expect.

print(3 < 5 == True)  # False

#This is not interpreted as:

#(3 < 5) and (5 == True)
#but as
#3 < 5 and 5 == True

#3 < 5 → True

#5 == True → False

#True and False → False
#if you want to group:

print((3 < 5) == True)  # True

#--------------------------------------------------------------

#What is the difference between & and and, | and or in Python?

#&, | → Bitwise operators
#Perform operation bit-by-bit on integers 

#and, or → Logical operators

# Bitwise
print(5 & 3)  # 101 & 011 = 001 → 1
print(5 | 3)  # 101 | 011 = 111 → 7

# Logical
print(True and False)  # False
print(0 and 10)         # 0 
print(5 or 0)           # 5 


# Arithmetic Operators
print(10 + 3)    # Addition
print(10 - 3)    # Subtraction
print(10 * 3)    # Multiplication
print(10 / 3)    # Division
print(10 ** 2)   # Exponential

#Assignment Operators
x = 5
x += 2      # x = x + 2 → 7
x -= 1      # x = x - 1 → 6
x *= 3      # x = x * 3 → 18
x //= 2     # x = x // 2 → 9
x %= 4      # x = x % 4 → 1
print(x)

#Comparison Operators
print(10 == 10)   # True
print(10 != 5)    # True
print(10 > 7)     # True
print(3 < 5)      # True
print(6 >= 6)     # True

#Logical Operators
print(True and False)     # False
print(True or False)      # True
print(not False)          # True
print(5 > 2 and 3 < 4)     # True
print(5 == 5 or 2 == 3)    # True

#Bitwise Operators
print(5 & 3)   # 0101 & 0011 → 0001 → 1
print(5 | 3)   # 0101 | 0011 → 0111 → 7
print(5 ^ 3)   # 0101 ^ 0011 → 0110 → 6
print(~5)      # Bitwise NOT → -6
print(5 << 1)  # Left shift → 10

#Identity Operators
a = 10
b = 10
print(a is b)         # True

x = [1, 2]
y = [1, 2]
print(x is y)         # False

print(x is not y)     # True

z = x
print(z is x)         # True

print(type(x) is list)  # True


#Membership Operators
print(2 in [1, 2, 3])        # True
print("a" in "apple")        # True
print("x" not in "hello")    # True
print(5 in range(10))        # True
print("hi" in ["hi", "hello"]) # True

#Ternary Operator
a = 5
b = 10
print("A is greater" if a > b else "B is greater")  # B is greater

num = -3
print("Positive" if num >= 0 else "Negative")  # Negative

x = 0
msg = "Zero" if x == 0 else "Non-zero"
print(msg)  # Zero

age = 18
print("Adult" if age >= 18 else "Minor")  # Adult

status = True
print("Active" if status else "Inactive")  # Active