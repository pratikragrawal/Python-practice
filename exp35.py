import math


numbera = int(input("Enter coefficient a: "))
numberb = int(input("Enter coefficient b: "))
numberc = int(input("Enter coefficient c: "))


discriminant = (numberb**2) - (4 * numbera * numberc)

if discriminant < 0:
    print("No real roots")
elif discriminant == 0:
    root = -numberb / (2 * numbera)
    print(f"One real root: {root}")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2 * numbera)
    root2 = (-b - math.sqrt(discriminant)) / (2 * numbera)
    print(f"Two real roots: {root1}, {root2}")