# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 28, 2025
# The program generates 10 random numbers and then find the min value

import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


def find_min_value(numbers):
    # Assume the first number is the smallest
    min_value = numbers[0]

    # Loop through the rest of the list
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def main():
    # Generate a list of 10 random numbers between 0 and 100
    numbers = []
    for _ in range(MAX_ARRAY_SIZE):
        rand_num = random.randint(MIN_NUM, MAX_NUM)
        numbers.append(rand_num)
        # Display the value
        print(f"The random number generated is:{rand_num}")

    # Find and print the minimum value
    minimum = find_min_value(numbers)
    print("Minimum value:", minimum)


if __name__ == "__main__":
    main()
