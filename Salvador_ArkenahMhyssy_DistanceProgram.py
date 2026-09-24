import math

# Calculates the distance between two points.
# Arkenah Mhyssy A. Salvador
# September 24, 2026

# Getting the distances of the points to compute
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Computing required calculations
distance_formula = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2-y1,2))

distance_result = round(distance_formula, 2)

# Display Results
print(f"\nThe distance between the two points is: {distance_result}")


# Reflection and Evaluation:

# Using a library is much more practical than coding all the calculations one by one for many reasons.
# Primarily, it contributed greatly in simplifying my program, as the library functions are not tedious, making the code easy to look at, and
# because the functions' size is very minimal and easily accessible, it saved me so much time and effort.
# If I didn't have "sqrt()"and "pow()" while making this program, it would be significantly harder and take so much of my time.