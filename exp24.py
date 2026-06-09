import math

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

hypotenuse = math.sqrt(side_a**2 + side_b**2)

print("The length of the hypotenuse is:", hypotenuse)
