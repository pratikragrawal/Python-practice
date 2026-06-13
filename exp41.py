def find_factorial(num):
    factorial = 1
    if num < 0:
        return "Sorry, factorial does not exist for negative numbers."
    elif num == 0:
        return "The factorial of 0 is 1."
    else:
        for i in range(1, num + 1):
            factorial *= i
        return f"The factorial of {num} is {factorial}."

# You can call this function with the number for which you want to find the factorial
number = 5  # Replace 5 with your desired number
result = find_factorial(number)
print(result)

