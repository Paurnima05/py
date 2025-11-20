# code for printing star pyramid
rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

    # code for printing inverted star pyramid
rows = int(input("Enter the number of rows for the inverted pyramid: "))

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# code for printing Star(*) diamond
rows = int(input("Enter the number of rows for the diamond: "))

# Ensure rows is odd
if rows % 2 == 0:
    rows += 1

# Upper half of the diamond
for i in range(rows // 2 + 1):
    for j in range(rows // 2 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half of the diamond
for i in range(rows // 2 - 1, -1, -1):
    for j in range(rows // 2 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
