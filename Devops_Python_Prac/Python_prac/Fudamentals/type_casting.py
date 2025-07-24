#What happens when you do: int("0010", 2)? Explain how Python handles base conversion.

print(int("0010", 2))  # Output: 2
#"0010" is a binary string (base 2).

#The int() function takes two arguments:
#int(string, base)
#So, int("0010", 2) means: Convert "0010" from base 2 → base 10.

#Binary:   0 0 1 0
#Decimal:      2
#Python strips leading zeros and correctly parses the binary value.

# can also be done using...
print(bin(2))  # '0b10'


#1. int() — Convert to Integer
#Converts float, bool, and numeric strings to integers 

print(int(3.9))         # ➝ 3
print(int("42"))        # ➝ 42
print(int(True))        # ➝ 1
print(int(False))       # ➝ 0
print(int("0b101", 2))  # ➝ 5 (binary to int)

#2. float() — Convert to Float
#Adds .0 to ints or numeric strings.

print(float(7))           
print(float("3.14"))      
print(float(True))         
print(float(False))      
print(float("2e2"))     

#3. str() — Convert to String
#Turns almost anything into a string.

print(str(100))           
print(str(3.14))          
print(str(True))          
print(str(None))          
print(str([1, 2, 3]))     


#4. bool() — Convert to Boolean

print(bool(0))            
print(bool(3.14))        
print(bool(""))           
print(bool("Python"))    
print(bool([]))           



#Not all conversions are valid:
int("3.14")  
float("abc")   
int("Hello")   
#Use try-except to catch conversion errors.