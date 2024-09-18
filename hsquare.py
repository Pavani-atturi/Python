side = int(input("Enter the size of the square: "))

# Loop through each row
for i in range(side):
    # Loop through each column
    for j in range(side):
        # Print '*' for the border elements
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print('*', end=' ')
        else:
            # Print space for the inner elements
            print(' ', end=' ')
    print()