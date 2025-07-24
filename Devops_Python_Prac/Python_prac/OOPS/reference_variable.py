#When we create object, it is stored in a variable. This variable called as reference variable.
class Customer:
    def __init__(self,name):
        self.name = name
def greet(customer):
    customer.name = "Shruti"
    print(customer.name)
    print(id(customer))
    
cust = Customer("Ruddhi")

greet(cust)
print(cust.name)
print(id(cust))

# if we pass any object to a function, and that function edits object then changes will be reflected in original object.
# this proves that object is mutable...(we can change it).just like lists , dictionary,sets.