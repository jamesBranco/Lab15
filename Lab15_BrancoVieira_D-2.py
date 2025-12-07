"""
Program: Lab 15, Cubes (#2)
Author: (James) Dyemydym Branco Vieira
Purpose: Answer both parts of question 15-1 in the TRY IT YOURSELF on page 315.
Date: 2025-12-01

"""

# Part ONE: Manually store the cubes of the first five numbers.
cubes_5 = [1, 8, 27, 64, 125]

print("Cubes of the first five numbers:")
for cube in cubes_5:
    print(cube)

print()  # Blank line for styling


# Part TWO: Use a loop to create the cubes of the first 5000 numbers.
cubes_5000 = []
for number in range(1, 5001):
    cube = number ** 3
    cubes_5000.append(cube)

print("Here are the first 10 cubes from the 5000 numbers:")
for cube in cubes_5000[:10]:
    print(cube)

print()
print("Total number of cubes generated:")
print(len(cubes_5000))
