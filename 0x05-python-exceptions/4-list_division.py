#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, ValueError, IndexError):
            is_invalid_type = not isinstance(my_list_1[i], (int, float)) or \
                              not isinstance(my_list_2[i], (int, float))
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            elif is_invalid_type:
                print("wrong type")
            else:
                print("division by 0")
            division_result = 0
        result.append(division_result)
    return (result)
