#!/usr/bin/python3
import sys


def add_arguments(*args):
    total = sum(int(arg) for arg in args)
    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python program.py [arg1] [arg2] ...")
    else:
        try:
            result = add_arguments(*sys.argv[1:])
            print(result)
        except ValueError as e:
            print("Error:", e)
