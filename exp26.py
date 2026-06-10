import math

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

# Calculate the semi-perimeter
s = (side_a + side_b + side_c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

print("The area of the triangle is:", area)
