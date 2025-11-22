class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


l1 = int(input("Enter the length of rect 1: "))
b1 = int(input("Enter the breadth of rect 1: "))
rect1 = Rectangle(l1, b1)

l2 = int(input("Enter the length of rect 2: "))
b2 = int(input("Enter the breadth of rect 2: "))
rect2 = Rectangle(l2, b2)

print("Area of rect 1 is:", rect1.area())
print("Perimeter of rect 1 is:", rect1.perimeter())
print("Area of rect 2 is:", rect2.area())
print("Perimeter of rect 2 is:", rect2.perimeter())

if rect1.area() > rect2.area():
    print("Area of rect 1 is greater")
else:
    print("Area of rect 2 is greater")