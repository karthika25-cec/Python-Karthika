from graphics.rectangle import area asrect_area, perimeter asrect_perimeter 
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics._3D_graphics.cuboid import surface_area as cuboid_surface_area, volume as 
cuboid_volume
from graphics._3D_graphics.sphere import surface_area assphere_surface_area, volume as 
sphere_volume
print("Enter the length and breadth of the rectangle:") 
l = int(input("Length: "))
b = int(input("Breadth: ")) 
print("Rectangle Area:", rect_area(l, b))
print("Rectangle Perimeter:", rect_perimeter(l, b)) 
print("\n\n")
print("Enter the radius of the circle:") 
radius = int(input("Radius: ")) 
print("Circle Area:", circle_area(radius))
print("Circle Perimeter:", circle_perimeter(radius))
print("\n\n")
print("Enter the dimensions of the cuboid:") 
length = float(input("Length: "))
width = float(input("Width: ")) 
height = float(input("Height: "))
print("Cuboid Surface Area:", cuboid_surface_area(length, width, height)) 
print("Cuboid Volume:", cuboid_volume(length, width, height)) 
print("\n\n")
print("Enter the radius of the sphere:") 
radius = float(input("Radius: "))
print("Sphere Surface Area:",sphere_surface_area(radius)) 
print("Sphere Volume:", sphere_volume(radius))