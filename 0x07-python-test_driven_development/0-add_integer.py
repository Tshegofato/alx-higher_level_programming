#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)


result = add_integer(5, 3.5)
print(result)
