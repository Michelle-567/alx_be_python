#Prompt User for Pattern Size:

size = int(input("Enter the size of the pattern: "))

# 2. Initialize row
row = 0

# 3. Draw pattern
while row < size:
    # For each row, print size number of "*"
    for col in range(size):
        print("*", end="")  # stay on the same line
    print()  # move to the next line
    row += 1
