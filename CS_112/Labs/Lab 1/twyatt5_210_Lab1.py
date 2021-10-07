#-------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: Lab 1
# Due Date: 9/3/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus. 
##-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments and assumptions: assume that user input will be decimal or base 10 
# or floats characters. 
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.
#-------------------------------------------------------------------------------

f0 = float(input('provide input '))
r = 2 ** (1/12)

f1 = f0 * r
f2 = f1 * r
f3 = f2 * r

print(round(f1, 2), round(f2, 2), round(f3, 2))