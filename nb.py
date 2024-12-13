n = int(input(""))  # Read the first number which tells how many numbers will follow

total_sum = 0  # Initialize the sum to 0

for _ in range(n):  # Loop through the next 'n' numbers
    num = int(input(""))  # Read each number
    total_sum += num  # Add it to the total sum

print(total_sum)  # Print the sum of the numbers
