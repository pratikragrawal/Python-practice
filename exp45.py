def is_palindrome(num):
    temp = num
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10
    if temp == reverse_num:
        return f"{temp} is a palindrome number."
    else:
        return f"{temp} is not a palindrome number."

# You can call this function with the number you want to check
number = 12321  # Replace 12321 with your desired number
result = is_palindrome(number)
print(result)

