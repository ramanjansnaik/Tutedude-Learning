#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
#o   Square root of the number
#o   Natural logarithm (log base e) of the number
#o   Sine of the number (in radians)
#3.   Displays the calculated results.
import math

n = int(input("Please enter your number: "))

print("square root of the number is: ", math.sqrt(n))
print("Natural log of number is :", math.log(n))
print("Sine of number is: ", math.sin(n))

