#!/usr/bin/env python3.9

# Python implemntion goes here

fahrenheit = float(input("What temperature (in Fahrenheit) would like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")