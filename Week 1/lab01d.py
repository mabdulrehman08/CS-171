import math

size=float(input("Enter size:\n"))
circle_radius= float(size/2)
area_circle= float( math.pi* circle_radius* circle_radius )
area_triangle= float( math.sqrt(3) /4 * size ** 2)
area_square=float(size*size)


print ("A circle of diameter",size ,"has an area of" , area_circle)
print ( "An equilateral triangle of size" ,size , "has an area of" ,area_triangle)
print ( "A square of size", size , "has an area of",area_square)

