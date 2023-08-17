#!/usr/bin/python3

def uniq_add(my_list=[]):
    total_sum = 0
    seen_numbers = {}
    for num in my_list:
        if num not in seen_numbers:
            total_sum += num
            seen_numbers[num] = True
    return total_sum
