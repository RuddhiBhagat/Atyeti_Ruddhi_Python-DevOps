"""
Q4.
You are given a list of numbers. Write a program to print only the first three odd numbers, skipping any negative numbers. 
If there are fewer than three odd numbers, print “Not enough odd numbers”.

"""
li = [1, 6, 4, 8, 5, 2]
res = []

for i in range(len(li)):
    if li[i] < 0:
        continue  
    if li[i] % 2 != 0:
        res.append(li[i])
        if len(res) == 3:
            break  
if len(res) == 3:
    print("First 3 odd numbers:", res)
else:
    print("Not enough odd numbers")
