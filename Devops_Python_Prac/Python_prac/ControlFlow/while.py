# Write a while loop that keeps accepting a number from the user and
# sums them up until the user enters a negative number.
sum = 0
n = int(input("Enter a number :  "))

while n >= 0:
    sum = sum + n
    n = int(input("Enter a new number : "))

print("Sum of entered numbers:", sum)

