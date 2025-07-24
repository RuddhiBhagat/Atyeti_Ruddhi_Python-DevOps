'''Q2.
Write a program that prints the following pattern using a for loop for n = 5:

*
**
***
**
*
'''
n = 5

#First part
for i in range(1, (n // 2) + 2):
    print('*' * i)

#Second part
for i in range(n // 2, 0, -1):
    print('*' * i)
