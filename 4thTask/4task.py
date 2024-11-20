animals = ["cat", "dog", "parrot"]
for animal in animals:
    print(f"Animal: {animal}")

n = 5
factorial = 1
counter = 1
while counter <= n:
    factorial *= counter
    counter += 1
print(f"Factorial of {n} is {factorial}")

colors = ["White", "Green", "Red"]
for index, color in enumerate(colors):
    print(f"Color at position {index} is {color}")
