seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = (seconds % 3600) % 60

print("The converted time is: {} hours, {} minutes, and {} seconds.".format(hours, minutes, remaining_seconds))
