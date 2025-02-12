# -*- coding: utf-8 -*-
"""assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c_cuWBkwVLg-SFiQoINU64JiHVjWtIhS
"""

#Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n
def sum_of_even_numbers(n):
    # Initialize sum to 0
    total = 0
    for i in range(2, n+1, 2):
        total += i

    return total

# Input: positive integer n
n = int(input("Enter a positive integer: "))

# Check if n is positive
if n > 0:
    result = sum_of_even_numbers(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
else:
    print("Please enter a positive integer.")



