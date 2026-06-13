def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return f"{num} is not a prime number."
        else:
            return f"{num} is a prime number."
    else:
        return f"{num} is not a prime number."

# You can call this function with the number you want to check
number = 17  # Replace 17 with your desired number
result = is_prime(number)
print(result)

