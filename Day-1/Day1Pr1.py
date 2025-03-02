list_a = []
list_b = []

with open("Day-1/input.txt", "r") as file:
    for line in file: 
        a, b = map(int, line.split())
        list_a.append(a)
        list_b.append(b)

# Sort the list before subtraction (by first number)
list_a.sort()
list_b.sort()

total_sum = 0  # Variable to store the total sum of differences

# Perform subtraction and store results
results = []
for a, b in zip(list_a, list_b):
    result = abs(a - b)
    results.append((a, b, result))
    total_sum += result

# Print sorted results
for a, b, result in results:
   print(f"{a} - {b} = {result}")

# Print the total sum of all results
print(f"\nTotal sum of differences: {total_sum}")


