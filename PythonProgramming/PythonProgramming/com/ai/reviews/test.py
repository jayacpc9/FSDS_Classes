import os
print("os.getcdw() :: ",os.getcwd())


my_list = ["Hello", "world", "from", "Python"]
print(my_list)

# Join with a space
result = " ".join(my_list)
print(result)  # Output: Hello world from Python

# Join with no separator
result_no_space = "".join(my_list)
print(result_no_space)  # Output: HelloworldfromPython

# Join with a comma
result_comma = ", ".join(my_list)
print(result_comma)  # Output: Hello, world, from, Python