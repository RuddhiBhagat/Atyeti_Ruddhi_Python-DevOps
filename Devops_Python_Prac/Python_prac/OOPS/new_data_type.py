# This is creating own data type using magic methods.(fraction operations are not supported in python.But using this we can create it.)
class Fraction:
    def __init__(self,n,d):
        self.n = n
        self.d = d

    def __str__(self):
        
        print("Hey! This is string method.")
        return f"{self.n}/{self.d}"

    def __add__(self,other):
        temp_num = self.n * other.d + self.d * other.n
        temp_deno = self.d * other.d
        return f"Adding given fraction:{temp_num}/{temp_deno}"

    def __sub__(self,other):
        temp_num = self.n * other.d - self.d *other.n
        temp_deno = self.d * other.d
        return f"Subtracting given fraction:{temp_num}/{temp_deno}"

    def __mul__(self,other):
        temp_num = self.n * other.n
        temp_deno = self.d * other.d
        return f"Multiplying given fraction:{temp_num}/{temp_deno}"

    def __truediv__(self,other):
        temp_num = self.n * other.d
        temp_deno = self.d * other.n
        return f"Dividing given fraction:{temp_num}/{temp_deno}"
x = Fraction(2,3)
y = Fraction(7,8)
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
