import math

#challange 1
d = 2000
t = 5
s = d / t
print("speed =", s, "m/s")

#challange 2
m = 200
v = 10
p = m / v
print("The dencity is", p)

#challange 3
n = 20
y = 5
x = (y / n) * 100
print("5 percent out of 20 is", x, "%")

# 4 (challenge): Find the values of x using the quadratic formula
a = 1
b = -8
c = 5

x_pos = (-b + math.sqrt(b**2 - 4 * a * c)) / (a * 2)
x_neg = (-b - math.sqrt(b**2 - 4 * a * c)) / (a * 2)

print("X positive is", x_pos)
print("X Negative is", x_neg)
