#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        error_message = "first_name must be string or last_name must be string"
        raise TypeError(error_message)
    print(f"My name is {first_name} {last_name}")


say_my_name("John", "Doe")
say_my_name("Alice")
