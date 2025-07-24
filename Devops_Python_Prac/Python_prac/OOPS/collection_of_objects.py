class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print("I am",self.name,"and I am",self.age,'.')

c1 = Customer("Ruddhi",22)
c2 = Customer("Shruti",22)
c3 = Customer("Shreya",23)

l = [c1,c2,c3]
for i in l:
    i.intro()