###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a= '))
b = int(input("b= "))
c = int(input("c= "))

surface_area = 2*(a*c + a*b + b*c)
volume = a*b*c

print(f"Surface_area: {surface_area}")
print(f"Volume: {volume}")