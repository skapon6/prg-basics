###
# Calculation of circle area and circumference 
#


# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

PI = 3.14
radius = int(input("Radius: "))
circumference = 2 * PI * radius
area = PI * radius**2 

print(f"""
      Results:
      radius : {radius}
      circumference : {circumference}
      area : {area}
      """)
