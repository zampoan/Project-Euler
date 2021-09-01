"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# How to solve the problem:
# 1. List all numbers which are below 10
# 2. Find those numbers that are divisible by 3 and 5
# 3. Add those numbers

number = 10
list_of_numbers =[]
def divide():
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_of_numbers.append(i)

    print(list_of_numbers)
    print(sum(list_of_numbers))

divide()
