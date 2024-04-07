eq = input("Enter the quadratic equation in the format '<a>x^2 + <b>x + <c> = 0': ") #The user enters an equation as a string
print(eq) #eq = '4x^2 +4x +    (-8) =  0'

# Extracting a, b, and c from user input and storing it to variables.
# ax^2+bx+c=0,a != 0
eq = eq.replace(' ', '')
elements_eq = eq.split('+')
a = int(elements_eq[0].replace('x^2', ''))
b = int(elements_eq[1].replace('x', ''))
c = int(elements_eq[2].replace('(', '').replace(')', '').replace('=0', ''))

print(a, b, c) # 4 4 -8

# Step 2. Calculate answer

from math import sqrt
d = (b ** 2 - 4 * a * c)
x1 = (- b + sqrt(d)) / (2*a)
x2 = (- b - sqrt(d)) / (2*a)

print(x1, x2) # 1, -2