'''suppose a,b and c length of the side of a triangle. then the area of a traiangle can be calculated
using the formula'''

import math
a = float(input("Enter the length of side a : "))
b = float(input("Enter the length of side b : "))
c = float(input("Enter the length of side c : "))

#calculate samiparimeter
s = (a+b+c)/2

# Calculate area using Heron's formula
area = math.sqrt(s*(s-a) * (s-b) * (s-c))

print(f"The area of a traiange is {area:.2f}")
