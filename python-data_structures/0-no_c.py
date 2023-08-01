def no_c(my_string):
    space = ""
    for char in my_string:
        if char != "c" and char != "C":
            space += char
    return space