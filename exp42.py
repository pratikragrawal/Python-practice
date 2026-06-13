def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is not an Armstrong number."

# You can call this function with the number you want to check
number = 153  # Replace 153 with your desired number
result = is_armstrong_number(number)
print(result)

