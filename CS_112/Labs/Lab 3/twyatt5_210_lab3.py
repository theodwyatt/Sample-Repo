# -------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: Lab 3
# Due Date: 9/17/2021
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus.
# -------------------------------------------------------------------------------
# References:
# -------------------------------------------------------------------------------
# Car insurance quotes:
#
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.

def car_insurance_qoute(car_price, age, accidents, promo):
    monthly_rate = 0
    if car_price <= 10000:
        monthly_rate =  car_price * .005
    elif 10000 < car_price < 25000:
        monthly_rate = car_price * .01
    else:
        monthly_rate = car_price * .02
        
    if 25 <= age < 39:
        monthly_rate -= (monthly_rate*.05)
    elif 40 <= age < 59:
        monthly_rate -= (monthly_rate*.10)
    elif age >= 60:
        monthly_rate -= (monthly_rate*.15)
        
    if promo == 'MASONPATRIOTS2021' and accidents == 'no':
        monthly_rate -= 10
    elif accidents == 'yes':
        monthly_rate += (monthly_rate *.20)
    return round(monthly_rate, 2)
print(car_insurance_qoute(23500, 19, 'yes', 'MASONPATRIOTS2021'))

