# Write a Python program to compute
# the distance between the points (x1, y1) and (x2, y2)


from math import sqrt

point1 = (3, 4)
point2 = (12, 20)

distance = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print(distance)
