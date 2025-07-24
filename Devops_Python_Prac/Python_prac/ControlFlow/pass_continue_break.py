numbers = [5, 0, -2, 7, 15, 0, 108, 3, 4]

for num in numbers:
    if num == 0:
        pass 
    elif num < 0:
        continue 
    elif num > 100:
        print(f"Number too large: {num}")
        break 
    print(f"Processing number: {num}")
