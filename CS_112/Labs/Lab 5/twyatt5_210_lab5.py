# -------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: lab 5
# Due Date: 10/01/2021
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus.
# -------------------------------------------------------------------------------
# References:
# -------------------------------------------------------------------------------
# Comments and assumptions: navigate a list using loops, assume lent of list is 
# >3 the function returns TRUE only when the condionis met for all item, otherwise
# return FALSE
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.
# -------------------------------------------------------------------------------


def equal_sum(numbers):
    for i in range(2, len(numbers)):
        if (numbers[i-1] + numbers[i-2]) != numbers[i]:
            return False
            break      
    return True
    

