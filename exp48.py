def convert_to_uppercase(input_string):
    result = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# You can call this function with the string you want to convert
input_str = "hello, world!"  # Replace "hello, world!" with your desired string
uppercase_str = convert_to_uppercase(input_str)
print(uppercase_str)
