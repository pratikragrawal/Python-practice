def fibonacci_series(term):
    a, b = 0, 1
    count = 0
    if term <= 0:
        return "Please enter a positive integer."
    elif term == 1:
        return "Fibonacci series up to", term, ":", a
    else:
        while count < term:
            print(a, end=" ")
            nth = a + b
            a = b
            b = nth
            count += 1

# Call this function with the term up to which you want to print the Fibonacci series
term = 10  # Replace 10 with your desired term
fibonacci_series(term)



