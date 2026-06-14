def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    return f"The sum of digits in the given number is: {sum}"

# You can call this function with the number for which you want to find the sum of digits
number = 12345  # Replace 12345 with your desired number
result = sum_of_digits(number)
print(result)





