#Calculating area of the circle
radius = 9
pi = 3.14
area = pi*radius*radius
print(area)
circum = 2*pi*radius
print(circum)

#Calculating slope of the circle
x = 5
y = 2*5-2
slope = x*y
print(slope)

#Calculating slope of point (2,2) and (6,10)
x = 2
y = 2
slope2 = y*2-y*1/x*2-x*1
print(slope2)

x = 6
y = 10
slope3 = y*2-y*1/x*2-x*1
print(slope3)

#Calculating Euclidean distance of point (2,2) and (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10

Euclidean_distance = (x1 - x2)-(y1 - y2)
print(Euclidean_distance)

#Compare the slopes in tasks 8 and 9
print(slope == slope2)

x = -3
y = x*x + 6*x +9
print(y)
