# Python Program to Solve Quadratic Equation
import cmath

a = 1
b = 5
c = 6

d = ((b **2) - (4 * a * c))

sol1 = (-b - cmath.sqrt(d)) / (2.0 * a)
sol2 = (-b + cmath.sqrt(d)) / (2.0 * a)

print(sol1, sol2)