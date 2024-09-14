import math

# Constant for gravity in m/s^2
g = 9.81

print("This program calculates distance traveled by a projectile on parabolic motion")

v = float(input("Input the initial velocity in m/s: "))
x_degrees = float(input("Input the initial angle in degrees: "))

# Convert angle from degrees to radians
x_radians = math.radians(x_degrees)

# Calculate the distance traveled in meters
distance_meters = (2 * v * v * math.sin(x_radians) * math.cos(x_radians)) / g

distance_miles = distance_meters * 0.000621371

print("Distance traveled in meters:   {:.2f}".format(distance_meters))
print("Distance traveled in miles :   {:.2f}".format(distance_miles))
