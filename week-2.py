# Create an empty list
# sourcery skip: merge-list-append
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1, 15)  # Index 1 corresponds to the second position

# Extend the list with another list
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.pop()  # This removes the last element (70)

# Sort the list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)

# Print the final list and the index of 30
print("Sorted list:", my_list)
print("Index of 30:", index_of_30)
