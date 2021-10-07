# -------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: Lab 4
# Due Date: 9/24/2021
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus.
# -------------------------------------------------------------------------------
# References:
# -------------------------------------------------------------------------------
# Loops: use operators such as +-*/ ** etc as needed.
#
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.


def calcSum(num):
    counter_num = 0
    for i in range(num):
        counter_num += i
    return counter_num


def calProduct(num):
    counter_prod = 1
    i = 1
    while i < num:
        counter_prod *= i
        i += 1
    return counter_prod


input_number = int(input('Pick a number: '))

my_sum = calcSum(input_number)
my_prod = calProduct(input_number)
print('Sum: ', my_sum)
print('Product: ', my_prod)
