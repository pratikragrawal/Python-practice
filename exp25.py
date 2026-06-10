principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

interest = (principal * rate * time) / 100

print("The simple interest is:", interest)
