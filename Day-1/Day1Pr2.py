list_a = []
list_b = []

with open("Day-1/input.txt", "r") as file:
    for line in file: 
        a, b = map(int, line.split())
        list_a.append(a)
        list_b.append(b)

# Calculate how many times a number from list_a exists in list_b
count = 0
for a in list_a:
    if a in list_b:
        count += 1 * a



print(f"Number of times a number from list_a exists in list_b: {count}")