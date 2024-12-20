# Create a set
my_set = {1, 2, 3, 4, 5}

# Add elements
my_set.add(6)
print("After adding 6:", my_set)

# Remove an element
my_set.remove(2)
print("After removing 2:", my_set)

# Discard an element that doesn't exist
my_set.discard(10)  
print("After discarding 10:", my_set)

# Pop an element
popped = my_set.pop()
print(f"Popped element: {popped}")
print("Set after pop:", my_set)

# Clear the set
my_set.clear()
print("After clearing the set:", my_set)
