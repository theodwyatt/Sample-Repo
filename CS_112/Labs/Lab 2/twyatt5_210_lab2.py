# -------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: Lab 2
# Due Date: 9/10/2021
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus.
# -------------------------------------------------------------------------------
# References:
# -------------------------------------------------------------------------------
# Comments and assumptions: assume the user is female who does not moderate
# exercise, the input you need from the user are: age, height, weight, and calorie
#
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.
# -------------------------------------------------------------------------------

def BMR(age, weight, height):
    BMR = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return BMR


def cal():
    calorie = (BMR(age, weight, height) * 1.55)
    return calorie


age = float(input('How old are you '))
weight = float(input('How much do you weigh '))
height = float(input('How tall are you '))
current_cal = float(input('How much is you daily calorie intake '))
percentage = round((current_cal / cal()) * 100, 2)

print('BMR:', round(BMR(age, weight, height), 2), 'kcal')
print('Ideal intake for a day is', round(cal(), 2), 'kcal.')
print('You are using this percent of you daily intake', percentage)
