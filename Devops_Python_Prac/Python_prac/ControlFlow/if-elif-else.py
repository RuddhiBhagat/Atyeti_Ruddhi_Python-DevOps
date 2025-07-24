'''Q1.
Write a program to take a number as input and print:

"Weird" if the number is odd.

"Weird" if the number is even and in the inclusive range of 6 to 20.

"Not Weird" if the number is even and in the inclusive range of 2 to 5 or greater than 20.'''


try:
    n = int(input("Enter number to be checked: "))
    print(f"Entered number is: {n}")

    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Number is not Valid")

except ValueError:
    print("Entered value is not an integer.")
