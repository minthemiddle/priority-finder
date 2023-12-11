import itertools

with open('options.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

# Define the goals array
goals = lines

# Create a dictionary to store the count of each item in the goals array
counts = {}
for goal in goals:
    counts[goal] = 1

# Generate all pairs of items from the goals array
pairs = itertools.combinations(goals, 2)

print(f"Enter your name:")
name = input().strip()
print(f"Which goal is more important?\nType 1 or 2 and hit enter")

# Prompt the user to pick one item from each pair and update the counts accordingly
for pair in pairs:
    while True:
        print(f"\n(1) {pair[0]} or  (2) {pair[1]}")
        choice = input().strip()
        if choice == '1':
            counts[pair[0]] += 1
            break
        elif choice == '2':
            counts[pair[1]] += 1
            break
        else:
            print("Decide what is more important. Enter 1 or 2.")

# Print the final counts for each item in the goals array
print(f"\nFinal priorities for: {name}")

for goal, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{goal}: {count}")

print(f"\nHow to read?")
print(f"Example: Goal 1 has count 4, Goal 2 has count 1")
print(f"👉 Goal 1 is 4x as important as Goal 2")

print(f"\nExplanation:")
print(f"For every chosen Goal, the priority is increased by 1")
print(f"Every Goal starts with count 1")
