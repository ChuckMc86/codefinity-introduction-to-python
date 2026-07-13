# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Task 1: Print how many times "apples" appear in the shelf
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

# Task 2: Store banana index in "banana_index" and print
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

# Task 3: Check if the number of apples is less than 5
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Task 4: Count how many times "grapes" appear on shelf
grapes_count = shelf.count("grapes")
if grapes_count <= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# Task 5: Check if "oranges" exist in the shelf tuple
orange_index = shelf.index("oranges")
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")
